# Clear
from tool_pencil import Pencil

class Clear:
    state = False

    # Constructor
    def __init__(self):
        pass
    
    # String representation
    def __str__(self):
        return f"Clear: {self.state}"
    
    def set_state(self, state: bool):
        self.state = state

    def clear_all(self, paint_surface, color, tool, drawn_history: dict):
        if self.state:
            # Remove imported image &
            # Remove (clear all) tools
            tool.get_pencil().clear()
            tool.get_pen().clear()
            tool.get_eraser().clear()
            tool.get_rectangle().clear()
            tool.get_circle().clear()
            # Clear all layers
            drawn_history.clear()
            # Set current layer to 0 (in main.py)

            # Fill with default background
            paint_surface.fill(color)
            # Set clear state to false again
            self.state = False
            return True
        return False