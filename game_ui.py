"""Window, fonts, colors, and reusable drawing helpers."""

import os

import pygame

WIDTH, HEIGHT, FPS = 1100, 700, 60
BG, PANEL, LIGHT = (10, 16, 31), (19, 29, 52), (29, 43, 72)
WHITE, MUTED, CYAN, GOLD, GREEN, RED = (232, 239, 250), (148, 166, 198), (88, 220, 228), (246, 194, 92), (112, 221, 164), (238, 112, 117)


def wrapped_lines(text, font, width):
    result, current = [], ""
    for word in text.split():
        trial = (current + " " + word).strip()
        if font.size(trial)[0] <= width:
            current = trial
        else:
            result.append(current)
            current = word
    if current:
        result.append(current)
    return result


class GameUI:
    def __init__(self, base_dir):
        pygame.init()
        pygame.display.set_caption("Last Light")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        asset_dir = os.path.join(base_dir, "assets")
        self.recharge = os.path.join(asset_dir, "recharge bd.otf")
        self.oxanium = os.path.join(asset_dir, "Oxanium-VariableFont_wght.ttf")
        self.font = pygame.font.Font(self.oxanium, 22)
        self.small = pygame.font.Font(self.oxanium, 17)
        self.sub = pygame.font.Font(self.recharge, 25)
        self.head = pygame.font.Font(self.recharge, 34)
        self.big = pygame.font.Font(self.recharge, 54)

    def draw_text(self, text, position, font=None, color=WHITE):
        self.screen.blit((font or self.font).render(text, True, color), position)

    def center(self, text, y, font=None, color=WHITE):
        image = (font or self.font).render(text, True, color)
        self.screen.blit(image, ((WIDTH - image.get_width()) // 2, y))

    def box(self, rect, color=PANEL, radius=12):
        pygame.draw.rect(self.screen, color, rect, border_radius=radius)

    def draw_hud(self, hero):
        self.box(pygame.Rect(22, 18, WIDTH - 44, 65))
        self.draw_text(f"{hero.name}  ·  {hero.calling}", (42, 30), self.font, CYAN)
        stats = f"HEALTH {max(0, hero.health)}   RESOLVE {hero.resolve}   CLUES {hero.clues}   TRUST {hero.trust}   STABILITY {hero.stability}"
        self.draw_text(stats, (42, 58), self.small, MUTED)
        self.draw_text("S save   L load   R restart   Esc title", (790, 42), self.small, MUTED)

