"""Player state for Last Light."""

from dataclasses import dataclass, field


@dataclass
class Hero:
    name: str = "Nova"
    calling: str = "Explorer"
    health: int = 3
    resolve: int = 2
    clues: int = 0
    trust: int = 0
    stability: int = 0
    flags: list[str] = field(default_factory=list)
    choices: list[str] = field(default_factory=list)
    last_result: str = ""
    scene: str = "opening"
    ending: str = ""

