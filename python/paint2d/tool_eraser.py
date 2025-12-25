# Eraser
import pygame


class Eraser:
    name = "eraser"
    state = False
    data = []
    color = (255, 255, 255)

    # Constructor
    def __init__(self):
        pass

    # String representation
    def __str__(self):
        return f"Eraser: {self.state} Data:= {self.data}"

    def set_state(self, state: bool):
        self.state = state

    # Draw eraser data
    def draw(self, pygame: pygame, surface: pygame.Surface):
        for element in self.data:
            coordinates = element[0]
            sizes = element[1]
            pygame.draw.circle(surface, self.color, (coordinates), sizes)

    # Append eraser data
    def append(
        self, mouse_x: int, mouse_y: int, size, drawn_history: dict, current_layer: int
    ):
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
