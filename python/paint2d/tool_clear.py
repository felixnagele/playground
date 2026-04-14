# Clear

from typing import Any


class Clear:
    state = False

    # Constructor
    def __init__(self) -> None:
        pass

    # String representation
    def __str__(self) -> str:
        return f"Clear: {self.state}"

    def set_state(self, state: bool) -> None:
        self.state = state

    def clear_all(
        self,
        paint_surface: Any,
        color: tuple[int, int, int],
        tool: Any,
        drawn_history: dict[int, Any],
    ) -> bool:
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
