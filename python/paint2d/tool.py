from typing import Any

from tool_circle import Circle
from tool_clear import Clear
from tool_eraser import Eraser
from tool_fill import Fill
from tool_pen import Pen
from tool_pencil import Pencil
from tool_rectangle import Rectangle


class Tool:
    tool_item_list = ["clear", "fill", "pencil", "pen", "eraser", "rectangle", "circle"]
    tool_image_path_pre = "rsc/img/tool_"
    tool_image_hover_path_pre = "rsc/img/tool_hover_"
    tool_image_list = [
        (f"{tool_image_path_pre}clear.png"),
        (f"{tool_image_path_pre}fill.png"),
        (f"{tool_image_path_pre}pencil.png"),
        (f"{tool_image_path_pre}pen.png"),
        (f"{tool_image_path_pre}eraser.png"),
        (f"{tool_image_path_pre}rectangle.png"),
        (f"{tool_image_path_pre}circle.png"),
    ]
    tool_image_hover_list = [
        (f"{tool_image_hover_path_pre}clear.png"),
        (f"{tool_image_hover_path_pre}fill.png"),
        (f"{tool_image_hover_path_pre}pencil.png"),
        (f"{tool_image_hover_path_pre}pen.png"),
        (f"{tool_image_hover_path_pre}eraser.png"),
        (f"{tool_image_hover_path_pre}rectangle.png"),
        (f"{tool_image_hover_path_pre}circle.png"),
    ]
    tool_states: dict[str, bool] = dict.fromkeys(tool_item_list, False)
    tool_object_dict: dict[str, Any] = {}

    # Tools
    clear: Clear
    fill: Fill
    pencil: Pencil
    pen: Pen
    eraser: Eraser
    rectangle: Rectangle
    circle: Circle

    def __init__(self) -> None:
        # ! Create the tools:
        self.clear = Clear()
        self.fill = Fill()
        self.pencil = Pencil()
        self.pen = Pen()
        self.eraser = Eraser()
        self.rectangle = Rectangle()
        self.circle = Circle()
        # ! Create the tool object dictionary:
        self.tool_object_dict = {
            self.tool_item_list[0]: self.clear,
            self.tool_item_list[1]: self.fill,
            self.tool_item_list[2]: self.pencil,
            self.tool_item_list[3]: self.pen,
            self.tool_item_list[4]: self.eraser,
            self.tool_item_list[5]: self.rectangle,
            self.tool_item_list[6]: self.circle,
        }

    def __str__(self) -> str:
        return f"Tool: {self.tool_object_dict}"

    def set_tool_state(self, tool: str, current_layer: int) -> int:
        if tool in self.tool_item_list:
            print(f"Tool: {tool}")
            # Set the selected tool to True and all other tools to False
            self.tool_states[tool] = True
            obj = self.tool_object_dict[tool]
            obj.set_state(True)
            current_layer += 1
            for i in range(len(self.tool_item_list)):
                if self.tool_item_list[i] != tool:
                    self.tool_states[self.tool_item_list[i]] = False
                    obj = self.tool_object_dict[self.tool_item_list[i]]
                    obj.set_state(False)
                    if self.tool_item_list[i] not in ["clear", "fill"]:
                        obj.clear()
            print(f"Tool states: {self.tool_states}")
            return current_layer
        return current_layer

    def is_tool_state(self, tool: str) -> bool:
        return self.tool_states[tool]

    # Getters
    def get_tool_object_dict(self) -> dict[str, Any]:
        return self.tool_object_dict

    def get_tool_item_list(self) -> list[str]:
        return self.tool_item_list

    def get_tool_image_list(self) -> list[str]:
        return self.tool_image_list

    def get_tool_image_hover_list(self) -> list[str]:
        return self.tool_image_hover_list

    def get_clear(self) -> Clear:
        return self.clear

    def get_fill(self) -> Fill:
        return self.fill

    def get_pencil(self) -> Pencil:
        return self.pencil

    def get_pen(self) -> Pen:
        return self.pen

    def get_eraser(self) -> Eraser:
        return self.eraser

    def get_rectangle(self) -> Rectangle:
        return self.rectangle

    def get_circle(self) -> Circle:
        return self.circle
