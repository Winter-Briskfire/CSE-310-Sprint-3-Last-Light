"""Main game state, input handling, persistence, and rendering."""

import json
import os
import sys
from dataclasses import asdict

import pygame

from game_ui import BG, CYAN, FPS, GOLD, GREEN, HEIGHT, LIGHT, MUTED, PANEL, RED, WHITE, WIDTH, GameUI, faded_color, wrapped_lines
from hero import Hero
from story import ENDINGS, OUTCOMES, SCENES

SAVE_FILE = "last_light_save.json"


class Game(GameUI):
    def __init__(self, base_dir):
        super().__init__(base_dir)
        self.hero = Hero()
        self.mode = "title"
        self.name = ""
        self.notice = ""
        self.notice_time = 0
        self.hover_choice = -1
        self.selected_choice = -1
        self.selected_until = 0

    def draw(self):
        self.screen.fill(BG)
        if self.mode == "title":
            self.center("LAST", 125, self.big, CYAN)
            self.center("LIGHT", 185, self.big, GOLD)
            self.center("A military-sci-fi adventure on the edge of the Eridani system", 260, self.font, MUTED)
            self.box(pygame.Rect(330, 350, 440, 145))
            self.center("Enter  Start mission", 378)
            self.center("L  Load mission", 418)
            self.center("Esc  Quit", 458, self.font, MUTED)
        elif self.mode == "name":
            self.center("IDENTIFY YOUR OPERATIVE", 145, self.head, CYAN)
            self.center("What should the unit call you?", 215, self.font, MUTED)
            self.box(pygame.Rect(315, 285, 470, 65), LIGHT)
            self.center(self.name or "Your callsign...", 302, self.head, WHITE if self.name else MUTED)
            self.center("Enter  Continue", 410, self.font, GOLD)
        elif self.mode == "ending":
            self.draw_ending()
        else:
            self.draw_scene()
        if self.notice_time > 0:
            self.box(pygame.Rect(320, HEIGHT - 55, 460, 38), LIGHT, 8)
            self.center(self.notice, HEIGHT - 48, self.small, GREEN)
        pygame.display.flip()

    def draw_scene(self):
        self.draw_hud(self.hero)
        title, body, choices = SCENES[self.hero.scene]
        self.draw_text(title, (60, 120), self.head, GOLD)
        pygame.draw.line(self.screen, CYAN, (60, 168), (WIDTH - 60, 168), 2)
        narrative = f"{self.hero.last_result} {body}" if self.hero.last_result else body
        y = 190
        for line in wrapped_lines(narrative, self.font, WIDTH - 130):
            self.draw_text(line, (60, y))
            y += 25
        prompt = "Select your class..." if self.hero.scene == "opening" else "What will you do?"
        self.draw_text(prompt, (60, 335), self.sub, CYAN)
        for index, (label, _, _) in enumerate(choices):
            rect = pygame.Rect(60, 380 + index * 68, WIDTH - 120, 54)
            hovered = rect.collidepoint(pygame.mouse.get_pos())
            active = hovered or index == self.selected_choice
            self.box(rect, faded_color(PANEL) if active else PANEL, 9)
            self.draw_text(str(index + 1), (78, rect.y + 13), self.head, GOLD)
            self.draw_text(label, (125, rect.y + 16))

    def draw_ending(self):
        self.draw_hud(self.hero)
        title, body = ENDINGS[self.hero.ending]
        self.center(title, 145, self.big, GOLD)
        self.center("MISSION COMPLETE", 220, self.head, CYAN)
        self.box(pygame.Rect(150, 290, 800, 150))
        y = 320
        for line in wrapped_lines(body, self.font, 730):
            self.center(line, y)
            y += 32
        aftermath = "The civilians you protected help rebuild Aurelia." if self.hero.trust >= 3 else "Eridani remembers your choices."
        self.center(aftermath, 485, self.font, GREEN if self.hero.trust >= 0 else RED)
        self.center("Enter  Play again       S  Save epilogue       Esc  Title", 575, self.font, MUTED)

    def start(self):
        self.hero = Hero()
        self.name = ""
        self.mode = "name"

    def select_choice(self, index):
        _, _, choices = SCENES[self.hero.scene]
        if not 0 <= index < len(choices):
            return
        if self.selected_until:
            return
        self.selected_choice = index
        self.selected_until = 8

    def apply_choice(self, index):
        _, _, choices = SCENES[self.hero.scene]
        if not 0 <= index < len(choices):
            return
        label, next_scene, changes = choices[index]
        self.hero.choices.append(label)
        self.hero.last_result = OUTCOMES.get(self.hero.scene, [""] * len(choices))[index]
        if self.hero.scene == "opening":
            self.hero.calling = label.split(" - ", 1)[0]
        for key, value in changes.items():
            if key == "flag" and value not in self.hero.flags:
                self.hero.flags.append(value)
            elif hasattr(self.hero, key):
                setattr(self.hero, key, getattr(self.hero, key) + value)
        if next_scene in ENDINGS:
            self.hero.ending = next_scene
            self.mode = "ending"
        else:
            self.hero.scene = next_scene
        self.selected_choice = -1

    def save(self):
        save_path = os.path.join(os.path.dirname(__file__), SAVE_FILE)
        with open(save_path, "w", encoding="utf-8") as file:
            json.dump(asdict(self.hero), file, indent=2)
        self.notice, self.notice_time = "Mission saved.", FPS * 2

    def load(self):
        save_path = os.path.join(os.path.dirname(__file__), SAVE_FILE)
        if not os.path.exists(save_path):
            self.notice = "No save file found."
        else:
            try:
                with open(save_path, encoding="utf-8") as file:
                    self.hero = Hero(**json.load(file))
                self.mode = "ending" if self.hero.ending else "scene"
                self.notice = "Mission loaded."
            except (OSError, TypeError, ValueError):
                self.notice = "That save file could not be loaded."
        self.notice_time = FPS * 2

    def handle_key(self, event):
        if event.key == pygame.K_ESCAPE:
            if self.mode == "title":
                pygame.quit()
                sys.exit()
            self.mode = "title"
            return
        if self.mode == "title":
            if event.key == pygame.K_RETURN:
                self.start()
            elif event.key == pygame.K_l:
                self.load()
        elif self.mode == "name":
            if event.key == pygame.K_RETURN and self.name.strip():
                self.hero.name = self.name.strip()[:18]
                self.mode = "scene"
            elif event.key == pygame.K_BACKSPACE:
                self.name = self.name[:-1]
            elif event.unicode.isprintable() and len(self.name) < 18:
                self.name += event.unicode
        elif self.mode == "ending":
            if event.key == pygame.K_RETURN:
                self.start()
            elif event.key == pygame.K_s:
                self.save()
        else:
            if event.key == pygame.K_s:
                self.save()
            elif event.key == pygame.K_l:
                self.load()
            elif event.key == pygame.K_r:
                self.start()
            elif pygame.K_1 <= event.key <= pygame.K_9:
                self.select_choice(event.key - pygame.K_1)

    def handle_mouse(self, position):
        """Handle clickable title-screen controls and story choices."""
        if self.mode == "title":
            if pygame.Rect(330, 350, 440, 52).collidepoint(position):
                self.start()
            elif pygame.Rect(330, 402, 440, 52).collidepoint(position):
                self.load()
        elif self.mode == "scene":
            for index in range(len(SCENES[self.hero.scene][2])):
                rect = pygame.Rect(60, 380 + index * 68, WIDTH - 120, 54)
                if rect.collidepoint(position):
                    self.select_choice(index)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    self.handle_key(event)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.handle_mouse(event.pos)
            if self.selected_until:
                self.selected_until -= 1
                if self.selected_until == 0:
                    self.apply_choice(self.selected_choice)
            if self.notice_time:
                self.notice_time -= 1
            self.draw()
            self.clock.tick(FPS)

