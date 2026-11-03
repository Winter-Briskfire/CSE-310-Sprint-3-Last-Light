"""Start Last Light."""

import os

from game import Game


if __name__ == "__main__":
    Game(os.path.dirname(os.path.abspath(__file__))).run()

