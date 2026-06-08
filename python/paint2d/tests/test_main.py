import pygame

import main
from menu import Menu
from tool import Tool
from tools_menu import ToolsMenu


# Main Tests:
def test_paint_surface_collision() -> None:
    # Initialize parameters
    mouse_x = 50
    mouse_y = 50
    paint_surface_offset_x = 10
    paint_surface_offset_y = 10
    paint_surface_width = 100
    paint_surface_height = 100

    # Test case 1: Mouse is within the paint surface
    result = main.paint_surface_collision(
        mouse_x,
        mouse_y,
        paint_surface_offset_x,
        paint_surface_offset_y,
        paint_surface_width,
        paint_surface_height,
    )
    if not result:
        raise AssertionError(f"Expected True, got {result}")

    # Test case 2: Mouse is outside the paint surface
    result = main.paint_surface_collision(
        200,
        200,
        paint_surface_offset_x,
        paint_surface_offset_y,
        paint_surface_width,
        paint_surface_height,
    )
    if result:
        raise AssertionError(f"Expected False, got {result}")


def test_convert_string_to_int() -> None:
    # Test case 1: Convert a valid string to an integer
    result = main.convert_string_to_int("42")
    if not result == 42:
        raise AssertionError(f"Expected 42, got {result}")

    # Test case 2: Convert an empty string to an integer (default value)
    result = main.convert_string_to_int("")
    if not result == 0:
        raise AssertionError(f"Expected 0, got {result}")

    # Test case 3: Attempt to convert an invalid string to an integer
    result = main.convert_string_to_int("abc")
    if not result == 0:
        raise AssertionError(f"Expected 0, got {result}")


def test_convert_int_to_string() -> None:
    # Test case 1: Convert a positive integer to a string
    result = main.convert_int_to_string(42)
    if not result == "42":
        raise AssertionError(f"Expected '42', got {result!r}")

    # Test case 2: Convert a negative integer to a string
    result = main.convert_int_to_string(-10)
    if not result == "-10":
        raise AssertionError(f"Expected '-10', got {result!r}")


def test_is_valid_size() -> None:
    # Test case 1: Valid size (within the range)
    result = main.is_valid_size(50)
    if not result:
        raise AssertionError(f"Expected truthy, got {result}")

    # Test case 2: Invalid size (below the range)
    result = main.is_valid_size(0)
    if result:
        raise AssertionError(f"Expected falsy, got {result}")

    # Test case 3: Invalid size (above the range)
    result = main.is_valid_size(150)
    if result:
        raise AssertionError(f"Expected falsy, got {result}")

    # Test case 4: Invalid size (not an integer)
    result = main.is_valid_size("invalid")
    if result:
        raise AssertionError(f"Expected falsy, got {result}")


def test_is_valid_hex_color() -> None:
    # Test case 1: Valid hex color code
    result = main.is_valid_hex_color("#3a4f87")
    if not result:
        raise AssertionError(f"Expected truthy, got {result}")

    # Test case 2: Valid hex color code with uppercase letters
    result = main.is_valid_hex_color("#ABCDEF")
    if not result:
        raise AssertionError(f"Expected truthy, got {result}")

    # Test case 3: Invalid hex color code (missing # symbol)
    result = main.is_valid_hex_color("3a4f87")
    if result:
        raise AssertionError(f"Expected falsy, got {result}")

    # Test case 4: Invalid hex color code (not 6 characters long)
    result = main.is_valid_hex_color("#abc")
    if result:
        raise AssertionError(f"Expected falsy, got {result}")

    # Test case 5: Invalid hex color code (contains invalid characters)
    result = main.is_valid_hex_color("#ghijkl")
    if result:
        raise AssertionError(f"Expected falsy, got {result}")


# Menu Tests:
def test_menu_init() -> None:
    window_width = 800
    window_height = 600
    main_surface = pygame.Surface((window_width, window_height))
    paint_surface = pygame.Surface((window_width, window_height))

    menu = Menu(window_width, window_height, main_surface, paint_surface)

    if not menu.window_width == window_width:
        raise AssertionError(f"Expected {window_width}, got {menu.window_width}")
    if not menu.window_height == window_height:
        raise AssertionError(f"Expected {window_height}, got {menu.window_height}")
    if not menu.main_surface == main_surface:
        raise AssertionError("Expected main_surface match")
    if not menu.paint_surface == paint_surface:
        raise AssertionError("Expected paint_surface match")
    if not len(menu.menu_item_list) > 0:
        raise AssertionError("Expected non-empty menu_item_list")
    if not isinstance(menu.menu_item_x, list):
        raise AssertionError("Expected menu_item_x to be a list")
    if not isinstance(menu.menu_item_y, list):
        raise AssertionError("Expected menu_item_y to be a list")
    if not isinstance(menu.menu_item_active, dict):
        raise AssertionError("Expected menu_item_active to be a dict")
    if not menu.menu_import_path == "rsc/imports/paint2d_import.png":
        raise AssertionError(f"Expected import path, got {menu.menu_import_path}")
    if not menu.menu_export_path == "rsc/exports/paint2d_export.png":
        raise AssertionError(f"Expected export path, got {menu.menu_export_path}")


# ToolMenu Tests:
def test_tools_menu_init() -> None:
    window_width = 800
    window_height = 600
    main_surface = pygame.Surface((window_width, window_height))
    paint_surface = pygame.Surface((window_width, window_height))

    tools_menu = ToolsMenu(window_width, window_height, main_surface, paint_surface)

    if not tools_menu.window_width == window_width:
        raise AssertionError(f"Expected {window_width}, got {tools_menu.window_width}")
    if not tools_menu.window_height == window_height:
        raise AssertionError(
            f"Expected {window_height}, got {tools_menu.window_height}"
        )
    if not tools_menu.main_surface == main_surface:
        raise AssertionError("Expected main_surface match")
    if not tools_menu.paint_surface == paint_surface:
        raise AssertionError("Expected paint_surface match")
    if not len(tools_menu.tool_item_list) > 0:
        raise AssertionError("Expected non-empty tool_item_list")
    if not len(tools_menu.tool_image_list) > 0:
        raise AssertionError("Expected non-empty tool_image_list")
    if not len(tools_menu.tool_image_hover_list) > 0:
        raise AssertionError("Expected non-empty tool_image_hover_list")
    if not isinstance(tools_menu.tool_item_active, dict):
        raise AssertionError("Expected tool_item_active to be a dict")
    if not isinstance(tools_menu.tool_item_selected, dict):
        raise AssertionError("Expected tool_item_selected to be a dict")
    if not isinstance(tools_menu.tool_item_hover, dict):
        raise AssertionError("Expected tool_item_hover to be a dict")


# Tool Tests:
def test_tool_init() -> None:
    tool = Tool()

    if not isinstance(tool.tool_object_dict, dict):
        raise AssertionError("Expected tool_object_dict to be a dict")
    expected_item_list = [
        "clear",
        "fill",
        "pencil",
        "pen",
        "eraser",
        "rectangle",
        "circle",
    ]
    if not tool.tool_item_list == expected_item_list:
        raise AssertionError(
            f"Expected {expected_item_list}, got {tool.tool_item_list}"
        )
    expected_image_list = [
        "rsc/img/tool_clear.png",
        "rsc/img/tool_fill.png",
        "rsc/img/tool_pencil.png",
        "rsc/img/tool_pen.png",
        "rsc/img/tool_eraser.png",
        "rsc/img/tool_rectangle.png",
        "rsc/img/tool_circle.png",
    ]
    if not tool.tool_image_list == expected_image_list:
        raise AssertionError(
            f"Expected {expected_image_list}, got {tool.tool_image_list}"
        )
    expected_hover_list = [
        "rsc/img/tool_hover_clear.png",
        "rsc/img/tool_hover_fill.png",
        "rsc/img/tool_hover_pencil.png",
        "rsc/img/tool_hover_pen.png",
        "rsc/img/tool_hover_eraser.png",
        "rsc/img/tool_hover_rectangle.png",
        "rsc/img/tool_hover_circle.png",
    ]
    if not tool.tool_image_hover_list == expected_hover_list:
        raise AssertionError(
            f"Expected {expected_hover_list}, got {tool.tool_image_hover_list}"
        )
    if not isinstance(tool.tool_states, dict):
        raise AssertionError("Expected tool_states to be a dict")
    if not len(tool.tool_states) == len(tool.tool_item_list):
        raise AssertionError(
            f"Expected {len(tool.tool_item_list)} states, got {len(tool.tool_states)}"
        )
    if not all(value is False for value in tool.tool_states.values()):
        raise AssertionError("Expected all tool states to be False")


def test_tool_set_tool_state() -> None:
    tool = Tool()

    # Test setting the state of a tool
    current_layer = 0
    new_layer = tool.set_tool_state("pencil", current_layer)
    if not tool.is_tool_state("pencil"):
        raise AssertionError("Expected pencil state to be True")
    if tool.is_tool_state("fill"):
        raise AssertionError("Expected fill state to be False")
    if tool.is_tool_state("rectangle"):
        raise AssertionError("Expected rectangle state to be False")
    if not new_layer == current_layer + 1:
        raise AssertionError(f"Expected {current_layer + 1}, got {new_layer}")

    # Test setting the state of a different tool
    new_layer = tool.set_tool_state("rectangle", new_layer)
    if tool.is_tool_state("pencil"):
        raise AssertionError("Expected pencil state to be False")
    if tool.is_tool_state("fill"):
        raise AssertionError("Expected fill state to be False")
    if not tool.is_tool_state("rectangle"):
        raise AssertionError("Expected rectangle state to be True")
    if not new_layer == current_layer + 2:
        raise AssertionError(f"Expected {current_layer + 2}, got {new_layer}")

    # Test setting the state of the same tool again
    new_layer = tool.set_tool_state("pencil", new_layer)
    if not tool.is_tool_state("pencil"):
        raise AssertionError("Expected pencil state to be True")
    if tool.is_tool_state("fill"):
        raise AssertionError("Expected fill state to be False")
    if tool.is_tool_state("rectangle"):
        raise AssertionError("Expected rectangle state to be False")
    if not new_layer == current_layer + 3:
        raise AssertionError(f"Expected {current_layer + 3}, got {new_layer}")


def test_tool_getters() -> None:
    tool = Tool()

    # Test getters
    tool_dict = tool.get_tool_object_dict()
    if not isinstance(tool_dict, dict):
        raise AssertionError("Expected tool_dict to be a dict")
    if not all(tool_item in tool_dict for tool_item in tool.tool_item_list):
        raise AssertionError("Expected all tool items in tool_dict")

    expected_item_list = [
        "clear",
        "fill",
        "pencil",
        "pen",
        "eraser",
        "rectangle",
        "circle",
    ]
    if not tool.get_tool_item_list() == expected_item_list:
        raise AssertionError(
            f"Expected {expected_item_list}, got {tool.get_tool_item_list()}"
        )
    expected_image_list = [
        "rsc/img/tool_clear.png",
        "rsc/img/tool_fill.png",
        "rsc/img/tool_pencil.png",
        "rsc/img/tool_pen.png",
        "rsc/img/tool_eraser.png",
        "rsc/img/tool_rectangle.png",
        "rsc/img/tool_circle.png",
    ]
    if not tool.get_tool_image_list() == expected_image_list:
        raise AssertionError(
            f"Expected {expected_image_list}, got {tool.get_tool_image_list()}"
        )
    expected_hover_list = [
        "rsc/img/tool_hover_clear.png",
        "rsc/img/tool_hover_fill.png",
        "rsc/img/tool_hover_pencil.png",
        "rsc/img/tool_hover_pen.png",
        "rsc/img/tool_hover_eraser.png",
        "rsc/img/tool_hover_rectangle.png",
        "rsc/img/tool_hover_circle.png",
    ]
    if not tool.get_tool_image_hover_list() == expected_hover_list:
        raise AssertionError(
            f"Expected {expected_hover_list}, got {tool.get_tool_image_hover_list()}"
        )

    if tool.get_clear() is None:
        raise AssertionError("Expected get_clear() to return non-None")
    if tool.get_fill() is None:
        raise AssertionError("Expected get_fill() to return non-None")
    if tool.get_pencil() is None:
        raise AssertionError("Expected get_pencil() to return non-None")
    if tool.get_pen() is None:
        raise AssertionError("Expected get_pen() to return non-None")
    if tool.get_eraser() is None:
        raise AssertionError("Expected get_eraser() to return non-None")
    if tool.get_rectangle() is None:
        raise AssertionError("Expected get_rectangle() to return non-None")
    if tool.get_circle() is None:
        raise AssertionError("Expected get_circle() to return non-None")
