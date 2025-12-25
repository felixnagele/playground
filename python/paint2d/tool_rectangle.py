# Rectangle
import pygame
import re

class Rectangle:
    name = "rectangle"
    state = False
    data_x = []
    data_y = []
    data_properties = []
    border = 1

    # Constructor
    def __init__(self):
        pass
    
    # String representation
    def __str__(self):
        return f"Rectangle: {self.state} Data(x, y):= {self.data_x}, {self.data_y}, {self.data_properties}"
    
    def set_state(self, state: bool):
        self.state = state
    
    # Draw rectangle data
    def draw(self, pygame: pygame, surface: pygame.Surface):
        for i in range(len(self.data_x)):
            properties = self.data_properties[i]
            sizes = properties[0]
            colors = properties[1]
            pygame.draw.rect(surface, colors, (self.data_x[i], self.data_y[i], sizes, sizes), self.border)
    
    # Append rectangle data
    def append(self, mouse_x: int, mouse_y: int, size, color, drawn_history: dict, current_layer: int):
        if self.state:
            applied_size = 1
            if self.is_valid_size(size):
                applied_size = size
            applied_color = (0, 0, 0)
            if self.is_valid_hex_color(color):
                applied_color = color
            self.data_x.append(mouse_x)
            self.data_y.append(mouse_y)
            self.data_properties.append([applied_size, applied_color])

            #print(f"X:{self.data_x} | Y:{self.data_y} | P:{self.data_properties}")

            drawn_history.update({current_layer: ((self.data_x, self.data_y, self.data_properties),self.name)})
    
    # Clear rectangle data
    def clear(self):
        self.data_x[:] = []
        self.data_y[:] = []

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
        hex_color_pattern = re.compile(r'^#([0-9a-fA-F]{6})$')

        # Check if the input string matches the pattern
        match = hex_color_pattern.match(hex_color)

        # Return True if there is a match, otherwise False
        return bool(match)