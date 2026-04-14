# Pencil

from typing import Any

import pygame


class Pencil:
    name = "pencil"
    state = False
    data_x: list[int] = []
    data_y: list[int] = []
    size = 1
    color = (0, 0, 0)

    # Constructor
    def __init__(self) -> None:
        pass

    # String representation
    def __str__(self) -> str:
        return f"Pencil: {self.state} Data(x, y):= {self.data_x}, {self.data_y}"

    def set_state(self, state: bool) -> None:
        self.state = state

    # Draw pencil data
    def draw(self, pygame: Any, surface: pygame.Surface) -> None:
        for i in range(len(self.data_x)):
            pygame.draw.rect(
                surface,
                self.color,
                (self.data_x[i], self.data_y[i], self.size, self.size),
            )

    # Append pencil data
    def append(
        self,
        mouse_x: int,
        mouse_y: int,
        drawn_history: dict[int, tuple[object, str]],
        current_layer: int,
    ) -> None:
        if self.state:
            self.data_x.append(mouse_x)
            self.data_y.append(mouse_y)
            # print(f"X:{self.data_x} | Y:{self.data_y}")
            drawn_history.update(
                {current_layer: ((self.data_x, self.data_y), self.name)}
            )

    # Clear pencil data
    def clear(self) -> None:
        self.data_x[:] = []
        self.data_y[:] = []
