# Pencil
import pygame

class Pencil:
    name = "pencil"
    state = False
    data_x = []
    data_y = []
    size = 1
    color = (0, 0, 0)

    # Constructor
    def __init__(self):
        pass
    
    # String representation
    def __str__(self):
        return f"Pencil: {self.state} Data(x, y):= {self.data_x}, {self.data_y}"
    
    def set_state(self, state: bool):
        self.state = state
    
    # Draw pencil data
    def draw(self, pygame: pygame, surface: pygame.Surface):
        for i in range(len(self.data_x)):
            pygame.draw.rect(surface, self.color, (self.data_x[i], self.data_y[i], self.size, self.size))
    
    # Append pencil data
    def append(self, mouse_x: int, mouse_y: int, drawn_history: dict, current_layer: int):
        if self.state:
            self.data_x.append(mouse_x)
            self.data_y.append(mouse_y)
            #print(f"X:{self.data_x} | Y:{self.data_y}")
            drawn_history.update({current_layer: ((self.data_x, self.data_y),self.name)})
    
    # Clear pencil data
    def clear(self):
        self.data_x[:] = []
        self.data_y[:] = []