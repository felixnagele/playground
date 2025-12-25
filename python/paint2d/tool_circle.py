# Circle
import pygame
import re


class Circle:
    name = "circle"
    state = False
    data = []
    border = 1

    # Constructor
    def __init__(self):
        pass

    # String representation
    def __str__(self):
        return f"Circle: {self.state} Data:= {self.data}"

    def set_state(self, state: bool):
        self.state = state

    # Draw circle data
    def draw(self, pygame: pygame, surface: pygame.Surface):
        for element in self.data:
            coordinates = element[0]
            sizes = element[1]
            colors = element[2]
            pygame.draw.circle(surface, colors, (coordinates), sizes, self.border)

    # Append circle data
    def append(
        self,
        mouse_x: int,
        mouse_y: int,
        size,
        color,
        drawn_history: dict,
        current_layer: int,
    ):
        if self.state:
            applied_size = 1
            if self.is_valid_size(size):
                applied_size = size
            applied_color = (0, 0, 0)
            if self.is_valid_hex_color(color):
                applied_color = self.hex_to_rgb(color)
            if applied_size == 1:
                self.data.append([(mouse_x, mouse_y), applied_size, applied_color])
            else:
                self.data.append([(mouse_x, mouse_y), applied_size // 2, applied_color])
            # print(self.data)

            drawn_history.update(
                {
                    current_layer: (
                        [(mouse_x, mouse_y), applied_size, applied_color],
                        self.name,
                    )
                }
            )

    # Clear circle data
    def clear(self):
        self.data[:] = []

    def is_valid_size(self, size):
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

    def is_valid_hex_color(self, hex_color):
        # Regular expression for a 24-bit color code in hexadecimal format
        hex_color_pattern = re.compile(r"^#([0-9a-fA-F]{6})$")

        # Check if the input string matches the pattern
        match = hex_color_pattern.match(hex_color)

        # Return True if there is a match, otherwise False
        return bool(match)

    def hex_to_rgb(self, hex_color):
        hex_color = hex_color.lstrip("#")
        return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))
