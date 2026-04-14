# Rectangle

from typing import Any

import pygame
import re


class Rectangle:
    name = "rectangle"
    state = False
    data_x: list[int] = []
    data_y: list[int] = []
    data_properties: list[list[Any]] = []
    border = 1

    # Constructor
    def __init__(self) -> None:
        pass

    # String representation
    def __str__(self) -> str:
        return f"Rectangle: {self.state} Data(x, y):= {self.data_x}, {self.data_y}, {self.data_properties}"

    def set_state(self, state: bool) -> None:
        self.state = state

    # Draw rectangle data
    def draw(self, pygame: Any, surface: pygame.Surface) -> None:
        for i in range(len(self.data_x)):
            properties = self.data_properties[i]
            sizes = properties[0]
            colors = properties[1]
            pygame.draw.rect(
                surface,
                colors,
                (self.data_x[i], self.data_y[i], sizes * 2, sizes * 2),
                self.border,
            )

    # Append rectangle data
    def append(
        self,
        mouse_x: int,
        mouse_y: int,
        size: int,
        color: str,
        drawn_history: dict[int, tuple[object, str]],
        current_layer: int,
    ) -> None:
        if self.state:
            applied_size = 1
            if self.is_valid_size(size):
                applied_size = size
            applied_color = (0, 0, 0)
            if self.is_valid_hex_color(color):
                applied_color = self.hex_to_rgb(color)
            self.data_x.append(mouse_x)
            self.data_y.append(mouse_y)
            self.data_properties.append([applied_size, applied_color])

            # print(f"X:{self.data_x} | Y:{self.data_y} | P:{self.data_properties}")

            drawn_history.update(
                {
                    current_layer: (
                        (self.data_x, self.data_y, self.data_properties),
                        self.name,
                    )
                }
            )

    # Clear rectangle data
    def clear(self) -> None:
        self.data_x[:] = []
        self.data_y[:] = []
        self.data_properties[:] = []

    def is_valid_size(self, size: object) -> bool:
        try:
            # Check if the value is an integer
            if not isinstance(size, int):
                return False

            # Check if the integer value is in the range (1, 100)
            if 0 < size <= 99:
                return True
            else:
                return False
        except ValueError:
            # If the value is not an integer, catch the ValueError
            return False

    def is_valid_hex_color(self, hex_color: str) -> bool:
        # Regular expression for a 24-bit color code in hexadecimal format
        hex_color_pattern = re.compile(r"^#([0-9a-fA-F]{6})$")

        # Check if the input string matches the pattern
        match = hex_color_pattern.match(hex_color)

        # Return True if there is a match, otherwise False
        return bool(match)

    def hex_to_rgb(self, hex_color: str) -> tuple[int, int, int]:
        hex_color = hex_color.lstrip("#")
        return (
            int(hex_color[0:2], 16),
            int(hex_color[2:4], 16),
            int(hex_color[4:6], 16),
        )
