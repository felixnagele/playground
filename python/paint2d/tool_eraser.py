# Eraser

from typing import Any

import pygame


class Eraser:
    name = "eraser"
    state = False
    data: list[list[Any]] = []
    color = (255, 255, 255)

    # Constructor
    def __init__(self) -> None:
        pass

    # String representation
    def __str__(self) -> str:
        return f"Eraser: {self.state} Data:= {self.data}"

    def set_state(self, state: bool) -> None:
        self.state = state

    # Draw eraser data
    def draw(self, pygame: Any, surface: pygame.Surface) -> None:
        for element in self.data:
            coordinates = element[0]
            sizes = element[1]
            pygame.draw.circle(surface, self.color, (coordinates), sizes)

    # Append eraser data
    def append(
        self,
        mouse_x: int,
        mouse_y: int,
        size: int,
        drawn_history: dict[int, tuple[object, str]],
        current_layer: int,
    ) -> None:
        if self.state:
            applied_size = 1
            if self.is_valid_size(size):
                applied_size = size
            self.data.append([(mouse_x, mouse_y), applied_size])
            # print(self.data)
            drawn_history.update(
                {current_layer: ([(mouse_x, mouse_y), applied_size], self.name)}
            )

    # Clear eraser data
    def clear(self) -> None:
        self.data[:] = []

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
