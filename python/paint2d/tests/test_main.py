import pygame
from main import *
from menu import *
from tools_menu import *
from tool import *


# Main Tests:
def test_paint_surface_collision():
    # Initialize parameters
    mouse_x = 50
    mouse_y = 50
    paint_surface_offset_x = 10
    paint_surface_offset_y = 10
    paint_surface_width = 100
    paint_surface_height = 100

    # Test case 1: Mouse is within the paint surface
    result = paint_surface_collision(
        mouse_x,
        mouse_y,
        paint_surface_offset_x,
        paint_surface_offset_y,
        paint_surface_width,
        paint_surface_height,
    )
    assert result is True

    # Test case 2: Mouse is outside the paint surface
    result = paint_surface_collision(
        200,
        200,
        paint_surface_offset_x,
        paint_surface_offset_y,
        paint_surface_width,
        paint_surface_height,
    )
    assert result is False


def test_convert_string_to_int():
    # Test case 1: Convert a valid string to an integer
    result = convert_string_to_int("42")
    assert result == 42

    # Test case 2: Convert an empty string to an integer (default value)
    result = convert_string_to_int("")
    assert result == 0

    # Test case 3: Attempt to convert an invalid string to an integer
    result = convert_string_to_int("abc")
    assert result == 0  # Should return the default value


def test_convert_int_to_string():
    # Test case 1: Convert a positive integer to a string
    result = convert_int_to_string(42)
    assert result == "42"

    # Test case 2: Convert a negative integer to a string
    result = convert_int_to_string(-10)
    assert result == "-10"


def test_is_valid_size():
    # Test case 1: Valid size (within the range)
    result = is_valid_size(50)
    assert result

    # Test case 2: Invalid size (below the range)
    result = is_valid_size(0)
    assert not result

    # Test case 3: Invalid size (above the range)
    result = is_valid_size(150)
    assert not result

    # Test case 4: Invalid size (not an integer)
    result = is_valid_size("invalid")
    assert not result


def test_is_valid_hex_color():
    # Test case 1: Valid hex color code
    result = is_valid_hex_color("#3a4f87")
    assert result

    # Test case 2: Valid hex color code with uppercase letters
    result = is_valid_hex_color("#ABCDEF")
    assert result

    # Test case 3: Invalid hex color code (missing # symbol)
    result = is_valid_hex_color("3a4f87")
    assert not result

    # Test case 4: Invalid hex color code (not 6 characters long)
    result = is_valid_hex_color("#abc")
    assert not result

    # Test case 5: Invalid hex color code (contains invalid characters)
    result = is_valid_hex_color("#ghijkl")
    assert not result


# Menu Tests:
def test_menu_init():
    window_width = 800
    window_height = 600
    main_surface = pygame.Surface((window_width, window_height))
    paint_surface = pygame.Surface((window_width, window_height))

    menu = Menu(window_width, window_height, main_surface, paint_surface)

    assert menu.window_width == window_width
    assert menu.window_height == window_height
    assert menu.main_surface == main_surface
    assert menu.paint_surface == paint_surface
    assert len(menu.menu_item_list) > 0
    assert isinstance(menu.menu_item_x, list)
    assert isinstance(menu.menu_item_y, list)
    assert isinstance(menu.menu_item_active, dict)
    assert menu.menu_import_path == "src/imports/paint2d_import.png"
    assert menu.menu_export_path == "src/exports/paint2d_export.png"


# ToolMenu Tests:
def test_tools_menu_init():
    window_width = 800
    window_height = 600
    main_surface = pygame.Surface((window_width, window_height))
    paint_surface = pygame.Surface((window_width, window_height))

    tools_menu = ToolsMenu(window_width, window_height, main_surface, paint_surface)

    assert tools_menu.window_width == window_width
    assert tools_menu.window_height == window_height
    assert tools_menu.main_surface == main_surface
    assert tools_menu.paint_surface == paint_surface
    assert len(tools_menu.tool_item_list) > 0
    assert len(tools_menu.tool_image_list) > 0
    assert len(tools_menu.tool_image_hover_list) > 0
    assert isinstance(tools_menu.tool_item_active, dict)
    assert isinstance(tools_menu.tool_item_selected, dict)
    assert isinstance(tools_menu.tool_item_hover, dict)


# Tool Tests:
def test_tool_init():
    tool = Tool()

    assert isinstance(tool.tool_object_dict, dict)
    assert tool.tool_item_list == [
        "clear",
        "fill",
        "pencil",
        "pen",
        "eraser",
        "rectangle",
        "circle",
    ]
    assert tool.tool_image_list == [
        "src/img/tool_clear.png",
        "src/img/tool_fill.png",
        "src/img/tool_pencil.png",
        "src/img/tool_pen.png",
        "src/img/tool_eraser.png",
        "src/img/tool_rectangle.png",
        "src/img/tool_circle.png",
    ]
    assert tool.tool_image_hover_list == [
        "src/img/tool_hover_clear.png",
        "src/img/tool_hover_fill.png",
        "src/img/tool_hover_pencil.png",
        "src/img/tool_hover_pen.png",
        "src/img/tool_hover_eraser.png",
        "src/img/tool_hover_rectangle.png",
        "src/img/tool_hover_circle.png",
    ]
    assert isinstance(tool.tool_states, dict)
    assert len(tool.tool_states) == len(tool.tool_item_list)
    assert all(value is False for value in tool.tool_states.values())


def test_tool_set_tool_state():
    tool = Tool()

    # Test setting the state of a tool
    current_layer = 0
    new_layer = tool.set_tool_state("pencil", current_layer)
    assert tool.is_tool_state("pencil")
    assert not tool.is_tool_state("fill")
    assert not tool.is_tool_state("rectangle")
    assert new_layer == current_layer + 1

    # Test setting the state of a different tool
    new_layer = tool.set_tool_state("rectangle", new_layer)
    assert not tool.is_tool_state("pencil")
    assert not tool.is_tool_state("fill")
    assert tool.is_tool_state("rectangle")
    assert new_layer == current_layer + 2

    # Test setting the state of the same tool again
    new_layer = tool.set_tool_state("pencil", new_layer)
    assert tool.is_tool_state("pencil")
    assert not tool.is_tool_state("fill")
    assert not tool.is_tool_state("rectangle")
    assert new_layer == current_layer + 3


def test_tool_getters():
    tool = Tool()

    # Test getters
    tool_dict = tool.get_tool_object_dict()
    assert isinstance(tool_dict, dict)
    assert all(tool_item in tool_dict for tool_item in tool.tool_item_list)

    assert tool.get_tool_item_list() == [
        "clear",
        "fill",
        "pencil",
        "pen",
        "eraser",
        "rectangle",
        "circle",
    ]
    assert tool.get_tool_image_list() == [
        "src/img/tool_clear.png",
        "src/img/tool_fill.png",
        "src/img/tool_pencil.png",
        "src/img/tool_pen.png",
        "src/img/tool_eraser.png",
        "src/img/tool_rectangle.png",
        "src/img/tool_circle.png",
    ]
    assert tool.get_tool_image_hover_list() == [
        "src/img/tool_hover_clear.png",
        "src/img/tool_hover_fill.png",
        "src/img/tool_hover_pencil.png",
        "src/img/tool_hover_pen.png",
        "src/img/tool_hover_eraser.png",
        "src/img/tool_hover_rectangle.png",
        "src/img/tool_hover_circle.png",
    ]

    assert tool.get_clear() is not None
    assert tool.get_fill() is not None
    assert tool.get_pencil() is not None
    assert tool.get_pen() is not None
    assert tool.get_eraser() is not None
    assert tool.get_rectangle() is not None
    assert tool.get_circle() is not None
