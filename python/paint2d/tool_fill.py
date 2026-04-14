# Fill

import re
from typing import Any


class Fill:
    name = "fill"
    state = False

    # Constructor
    def __init__(self) -> None:
        pass

    # String representation
    def __str__(self) -> str:
        return f"Fill: {self.state}"

    def set_state(self, state: bool) -> None:
        self.state = state

    def fill(self, paint_surface: Any, color: str) -> None:
        if self.state:
            if self.is_valid_hex_color(color):
                paint_surface.fill(color)

    def is_valid_hex_color(self, hex_color: str) -> bool:
        # Regular expression for a 24-bit color code in hexadecimal format
        hex_color_pattern = re.compile(r"^#([0-9a-fA-F]{6})$")

        # Check if the input string matches the pattern
        match = hex_color_pattern.match(hex_color)

        # Return True if there is a match, otherwise False
        return bool(match)
