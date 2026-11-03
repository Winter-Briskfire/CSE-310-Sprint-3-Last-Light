# Last Light

Sprint 3 is an original military-science-fiction PyGame choose-your-own-adventure set in the Eridani system during a planetary invasion. It features four operative roles, persistent consequences, and multiple endings in a graphical interface with a data-driven story structure.

## Run the game

1. Install Python 3.10 or newer.
2. Install PyGame with `python -m pip install -r requirements.txt`.
3. Start the game with `python main.py`.

### Standalone executable

You can also double-click `LastLight.exe` in this folder. It is a standalone Windows build and does not require VS Code, PowerShell, Python, or PyGame to be installed.

## Controls

- Use the mouse or number keys to choose an option. Hovering over or selecting a button fades it by about 50% for visual feedback.
- `Enter` starts the game and confirms the operative's name.
- `S` saves to `last_light_save.json`; `L` loads it.
- `R` restarts the current mission; `Esc` returns to the title screen.

## Improvements from Sprint 1

- PyGame interface drawn in code, so no image assets are required.
- Data-driven scenes make branching story content easy to expand.
- Mouse and keyboard support.
- JSON save/load support.
- HUD for health, resolve, clues, civilian trust, and signal stability.
- Four distinct starting callings and four endings.
- Consequences carry forward through flags and stats.
- Recharge is used for the title and headers; Oxanium is used for body and interface text.
- The setting and title are entirely new: the story now takes place in the Eridani system, where operatives defend the colony world Aurelia during a last-stand evacuation.
- The tone draws from military sci-fi and desperate last-stand stories while using original locations, factions, characters, and plot.
- Every choice now produces a written field result that explains how it leads into the next scenario.
- Code is split into `main.py`, `game.py`, `game_ui.py`, `hero.py`, and `story.py`, following the organized structure of the original C++ project.

## Course requirement alignment

The Choose Your Own Adventure module allows the student to propose the software and requirements. This project proposes the following five requirements:

1. Provide four playable classes with distinct opening scenarios.
2. Provide a graphical PyGame interface with mouse and keyboard input.
3. Track persistent consequences including health, resolve, clues, trust, stability, and unlocked flags.
4. Provide connected branching scenes with immediate decision results and multiple endings.
5. Organize the project into separate modules with comments and a professional README.

Implementation checklist:

- [x] Original PyGame software and story content.
- [x] Five proposed project requirements implemented.
- [x] Stretch challenge implemented: save and load the mission as JSON.
- [x] README included at the top of the Sprint Three folder.
- [x] Useful comments and modular source files included.
- [ ] Submit the sprint plan for instructor pre-approval before the deadline.
- [ ] Record and publish an execution and code-walkthrough video.
- [ ] Publish the completed module and README in the public GitHub repository.

## Development environment

- Python 3.10+
- PyGame 2.5+
- Standard library modules: `json`, `dataclasses`, `os`, and `sys`
- Included fonts: `assets/recharge bd.otf` and `assets/Oxanium-VariableFont_wght.ttf`

## Future work

- [ ] Add music and sound effects.
- [ ] Add illustrated backgrounds for the four starting locations.
- [ ] Add more scenes and a map showing visited branches.
