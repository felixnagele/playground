#!/usr/bin/env python3
from menu import Menu
from tools_menu import ToolsMenu
from tool import Tool
import pygame
import sys
import time
import re

# ! Initialize global variables
DEFAULT_main_surface_WIDTH = 1200
DEFAULT_main_surface_HEIGHT = 700
mouse_x = 0
mouse_y = 0
paint_surface_offset_x = 20
paint_surface_offset_y = 125
paint_surface_width = 500
paint_surface_height = 500
PAINT_BACKGROUND_COLOR = (255, 255, 255)
paint_surface = pygame.Surface((paint_surface_width, paint_surface_height))
paint_surface.fill(PAINT_BACKGROUND_COLOR)
imported_image = None
size_color_field_offset_x = 75


def main():
    # Define main variables
    global mouse_x
    global mouse_y
    global PAINT_BACKGROUND_COLOR
    global imported_image

    # Define window variables
    global DEFAULT_main_surface_WIDTH
    global DEFAULT_main_surface_HEIGHT
    WINDOW_CAPTION = "Paint2D"
    WINDOW_ICON_PATH = "src/img/paint2d_icon.png"

    # Define paint surface variables
    global paint_surface
    global paint_surface_offset_x
    global paint_surface_offset_y
    global paint_surface_width
    global paint_surface_height
    x_item_text = convert_int_to_string(paint_surface_width)
    y_item_text = convert_int_to_string(paint_surface_height)
    x_item_text_active = False
    y_item_text_active = False
    size_text_active = False
    color_text_active = False
    x_y_location_list = []
    selected_size = convert_int_to_string(1)  # Default 1
    selected_color = "#000000"  # Default Black
    size_color_font_size = 26
    global size_color_field_offset_x
    cursor_timer = time.time()

    # Check if valid
    if not is_valid_size(convert_string_to_int(selected_size)):
        print("Error: The size is not valid.")
    if not is_valid_hex_color(selected_color):
        print("Error: The color is not valid.")

    # Define color constants
    WINDOW_BACKGROUND_COLOR = (200, 200, 200)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Define state variables
    running = True
    drawing = False
    cursor_visible = True

    # Define painting variables
    paint_mouse_x = 0
    paint_mouse_y = 0

    # Draw per layer
    # Dictionary to store drawn shapes and their layers
    drawn_history = {}
    # Current layer
    current_layer = -1  # Default -1
    # Current drawing type
    current_type = None

    # Initialize drawn_history
    # First layer = 0
    # drawn_history[0] = []

    # Initialize Pygame
    pygame.init()

    # ! Create the Pygame window and settings
    main_surface = pygame.display.set_mode(
        (DEFAULT_main_surface_WIDTH, DEFAULT_main_surface_HEIGHT), pygame.RESIZABLE
    )
    # Set Window Title
    pygame.display.set_caption(WINDOW_CAPTION)
    # Set Window Icon
    icon = pygame.image.load(WINDOW_ICON_PATH)
    pygame.display.set_icon(icon)

    # ! Create the menu
    menu = Menu(
        DEFAULT_main_surface_WIDTH,
        DEFAULT_main_surface_HEIGHT,
        main_surface,
        paint_surface,
    )
    print(menu)

    # ! Create the tools menu
    tools_menu = ToolsMenu(
        DEFAULT_main_surface_WIDTH,
        DEFAULT_main_surface_HEIGHT,
        main_surface,
        paint_surface,
    )
    print(tools_menu)

    # ! Create the tool
    tool = Tool()
    print(tool)

    # ! Main loop
    while running:
        # * Update Menu
        menu.window_update(main_surface, paint_surface)

        # * Menu Status
        menu_item_active = menu.get_menu_item_active()
        menu_item_list = menu.get_menu_item_list()

        # * Menu Item Actions
        if menu_item_active[menu_item_list[0]]:  # Import
            clear_imported_image()
            imported_image = menu.import_image(pygame)
            if (
                imported_image.get_width()
                < DEFAULT_main_surface_WIDTH
                - paint_surface_offset_x
                - tools_menu.get_offset_x()
                and imported_image.get_height()
                < DEFAULT_main_surface_HEIGHT
                - paint_surface_offset_y
                - tools_menu.get_offset_y()
            ):  # If the image fits in the paint surface, update the paint surface
                x_item_text = convert_int_to_string(imported_image.get_width())
                y_item_text = convert_int_to_string(imported_image.get_height())
                paint_surface_update(
                    x_item_text,
                    y_item_text,
                    PAINT_BACKGROUND_COLOR,
                    tools_menu.get_offset_x(),
                    tools_menu.get_offset_y(),
                )
            else:
                imported_image = None
                paint_surface_update(
                    x_item_text,
                    y_item_text,
                    PAINT_BACKGROUND_COLOR,
                    tools_menu.get_offset_x(),
                    tools_menu.get_offset_y(),
                )
            menu_item_active[menu_item_list[0]] = False
        if menu_item_active[menu_item_list[1]]:  # Export
            menu.export_image(pygame)
            paint_surface_update(
                x_item_text,
                y_item_text,
                PAINT_BACKGROUND_COLOR,
                tools_menu.get_offset_x(),
                tools_menu.get_offset_y(),
            )
            menu_item_active[menu_item_list[1]] = False
        if menu_item_active[menu_item_list[2]]:  # Dimension
            clear_imported_image()
            paint_surface_update(
                x_item_text,
                y_item_text,
                PAINT_BACKGROUND_COLOR,
                tools_menu.get_offset_x(),
                tools_menu.get_offset_y(),
            )
            menu_item_active[menu_item_list[2]] = False
        if menu_item_active[menu_item_list[3]]:  # X Item
            y_item_text_active = False
            size_text_active = False
            color_text_active = False
            x_item_text_active = True
            menu_item_active[menu_item_list[3]] = False
        if menu_item_active[menu_item_list[4]]:  # Y Item
            x_item_text_active = False
            size_text_active = False
            color_text_active = False
            y_item_text_active = True
            menu_item_active[menu_item_list[4]] = False

        # * Update ToolsMenu
        tools_menu.update(main_surface, paint_surface)

        # * ToolsMenu Status
        tool_item_active = tools_menu.get_tool_item_active()
        tool_item_list = tools_menu.get_tool_item_list()

        # * ToolsMenu Item Actions
        for i in range(len(tool_item_list)):
            if tool_item_active[tool_item_list[i]]:
                # Set i tool with active state
                current_layer = tool.set_tool_state(tool_item_list[i], current_layer)
                # print(current_layer)
                print(drawn_history)
                # Set i tool with active state False again
                tool_item_active[tool_item_list[i]] = False

        # ! Draw
        # Draw main_surface with light grey background
        main_surface.fill(WINDOW_BACKGROUND_COLOR)
        # Add the paint_surface to the main_surface
        main_surface.blit(
            paint_surface, (paint_surface_offset_x, paint_surface_offset_y)
        )
        # Apply imported image to paint surface
        if (
            imported_image != None
            and x_item_text == convert_int_to_string(imported_image.get_width())
            and y_item_text == convert_int_to_string(imported_image.get_height())
        ):
            paint_surface = imported_image.convert()

        # * Draw menu items
        menu.draw_import_export(pygame)
        menu.draw_dimension(pygame)
        x_y_location_list = menu.get_x_y_location_list()
        menu.draw_max_x_y(
            pygame,
            convert_int_to_string(
                DEFAULT_main_surface_WIDTH
                - paint_surface_offset_x
                - tools_menu.get_offset_x()
                - size_color_field_offset_x
            ),
            convert_int_to_string(
                DEFAULT_main_surface_HEIGHT
                - paint_surface_offset_y
                - tools_menu.get_offset_y()
            ),
        )

        # Create text_surface for X and Y item & selected size, color
        # X, Y
        font = pygame.font.Font(None, menu.get_x_y_font_size())
        text_x_surface = font.render(x_item_text, True, BLACK)
        text_y_surface = font.render(y_item_text, True, BLACK)

        # size, color
        size_field_location = tools_menu.get_size_field_location()
        color_field_location = tools_menu.get_color_field_location()
        font = pygame.font.Font(None, size_color_font_size)
        if len(selected_size) < 1 or selected_size == "0" or selected_size == "00":
            text_size_surface = font.render("1", True, BLACK)
        else:
            text_size_surface = font.render(selected_size, True, BLACK)
        text_color_surface = font.render(selected_color, True, BLACK)

        # Add input of X and Y Item to main_surface & size, color
        main_surface.blit(text_x_surface, (x_y_location_list[0], x_y_location_list[1]))
        main_surface.blit(text_y_surface, (x_y_location_list[2], x_y_location_list[3]))
        main_surface.blit(
            text_size_surface, (size_field_location[0], size_field_location[1])
        )  # Store in list (generated in main)
        main_surface.blit(
            text_color_surface, (color_field_location[0], color_field_location[1])
        )

        # Draw Cursor for X and Y Item
        if time.time() - cursor_timer > 0.5:
            cursor_visible = not cursor_visible
            cursor_timer = time.time()

        # Toggle the cursor & add input in X and Y Item
        if cursor_visible:
            if x_item_text_active:
                cursor_surface_x_item_text = font.render("_", True, BLACK)
                cursor_x_item_text = x_y_location_list[0] + text_x_surface.get_width()
                main_surface.blit(
                    cursor_surface_x_item_text,
                    (cursor_x_item_text, x_y_location_list[1]),
                )
            if y_item_text_active:
                cursor_surface_y_item_text = font.render("_", True, BLACK)
                cursor_y_item_text = x_y_location_list[2] + text_y_surface.get_width()
                main_surface.blit(
                    cursor_surface_y_item_text,
                    (cursor_y_item_text, x_y_location_list[3]),
                )
            if size_text_active:
                cursor_surface_size_text = font.render("_", True, BLACK)
                cursor_size_text = (
                    size_field_location[0] + text_size_surface.get_width()
                )
                main_surface.blit(
                    cursor_surface_size_text, (cursor_size_text, size_field_location[1])
                )
            if color_text_active:
                cursor_surface_color_text = font.render("_", True, BLACK)
                cursor_color_text = (
                    color_field_location[0] + text_color_surface.get_width()
                )
                main_surface.blit(
                    cursor_surface_color_text,
                    (cursor_color_text, color_field_location[1]),
                )

        # * Draw tools menu items
        tools_menu.draw(pygame)
        tools_menu.draw_size_color_fields(pygame)
        tools_menu.draw_selected_tool(pygame)
        tools_menu.draw_hover_tool(pygame)

        # * Use tools
        # (mostly draw and draw_on_mouse functions)

        # Clear
        clear_state = tool.get_clear().clear_all(
            paint_surface, PAINT_BACKGROUND_COLOR, tool, drawn_history
        )
        if clear_state:
            imported_image = None
            current_layer = 0
        # Update the display to render all shapes in the history
        for layer in sorted(drawn_history.keys()):
            for tool_item_type in drawn_history[layer]:
                if tool_item_type == "pencil":
                    tool.get_pencil().draw(pygame, paint_surface)
                elif tool_item_type == "pen":
                    tool.get_pen().draw(pygame, paint_surface)
                elif tool_item_type == "eraser":
                    tool.get_eraser().draw(pygame, paint_surface)
                elif tool_item_type == "rectangle":
                    tool.get_rectangle().draw(pygame, paint_surface)
                elif tool_item_type == "circle":
                    tool.get_circle().draw(pygame, paint_surface)

        # Fill
        tool.get_fill().fill(paint_surface, selected_color)

        # ! Handle events
        # * Get mouse position per layer (surface)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # * Get mouse position from paint surface
        paint_mouse_x = mouse_x - paint_surface_offset_x
        paint_mouse_y = mouse_y - paint_surface_offset_y

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                # Update the main_surface width and height when the window is resized
                DEFAULT_main_surface_WIDTH, DEFAULT_main_surface_HEIGHT = (
                    event.w,
                    event.h,
                )
                main_surface = pygame.display.set_mode(
                    (DEFAULT_main_surface_WIDTH, DEFAULT_main_surface_HEIGHT),
                    pygame.RESIZABLE,
                )
                print(
                    "Window resized to:",
                    DEFAULT_main_surface_WIDTH,
                    DEFAULT_main_surface_HEIGHT,
                )
                # Update the tools menu sizes when the window is resized
                tools_menu.update_window(
                    DEFAULT_main_surface_WIDTH,
                    DEFAULT_main_surface_HEIGHT,
                    main_surface,
                    paint_surface,
                )
                print(tools_menu)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_BACKSPACE:
                    # X
                    if x_item_text_active:
                        x_item_text = x_item_text[:-1]
                    # Y
                    if y_item_text_active:
                        y_item_text = y_item_text[:-1]
                    # Size
                    if size_text_active:
                        selected_size = selected_size[:-1]
                    # Color
                    if color_text_active:
                        if selected_color != "#":
                            selected_color = selected_color[:-1]
                elif pygame.K_0 <= event.key <= pygame.K_9:
                    # Convert the key to a integer
                    if x_item_text_active:
                        if len(x_item_text) < 4:
                            x_item_text += event.unicode
                    if y_item_text_active:
                        if len(y_item_text) < 4:
                            y_item_text += event.unicode
                    # Selected size
                    if size_text_active:
                        if len(selected_size) < 2:
                            if len(selected_size) < 1 and event.unicode == "0":
                                pass
                            else:
                                selected_size += event.unicode
                    # Selected color
                    if color_text_active:
                        if len(selected_color) < 7:
                            selected_color += event.unicode
                elif pygame.K_a <= event.key <= pygame.K_f:
                    # Selected color
                    if color_text_active:
                        if len(selected_color) < 7:
                            selected_color += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print("Left mouse button pressed")
                    # Interacting with menu items if mouse is within at least one menu item
                    menu.collision(mouse_x, mouse_y)
                    # Interacting with tools menu items if mouse is within at least one tools menu item
                    tools_menu.collision(mouse_x, mouse_y)
                    # * Size, Color Tool Properties Collisions:
                    # Size
                    if tools_menu.collision_size_field(mouse_x, mouse_y):
                        color_text_active = False
                        x_item_text_active = False
                        y_item_text_active = False
                        size_text_active = True
                    # Color
                    if tools_menu.collision_color_field(mouse_x, mouse_y):
                        size_text_active = False
                        x_item_text_active = False
                        y_item_text_active = False
                        color_text_active = True
                    # Interact with paint_surface if mouse is within the paint surface
                    drawing = True
                    if paint_surface_collision(
                        mouse_x,
                        mouse_y,
                        paint_surface_offset_x,
                        paint_surface_offset_y,
                        paint_surface_width,
                        paint_surface_height,
                    ):
                        # Pencil
                        tool.get_pencil().append(
                            paint_mouse_x, paint_mouse_y, drawn_history, current_layer
                        )
                        # Pen
                        tool.get_pen().append(
                            paint_mouse_x,
                            paint_mouse_y,
                            convert_string_to_int(selected_size),
                            selected_color,
                            drawn_history,
                            current_layer,
                        )
                        # Eraser
                        tool.get_eraser().append(
                            paint_mouse_x,
                            paint_mouse_y,
                            convert_string_to_int(selected_size),
                            drawn_history,
                            current_layer,
                        )
                        # Rectangle
                        tool.get_rectangle().append(
                            paint_mouse_x,
                            paint_mouse_y,
                            convert_string_to_int(selected_size),
                            selected_color,
                            drawn_history,
                            current_layer,
                        )
                        # Circle
                        tool.get_circle().append(
                            paint_mouse_x,
                            paint_mouse_y,
                            convert_string_to_int(selected_size),
                            selected_color,
                            drawn_history,
                            current_layer,
                        )
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    print("Left mouse button released")
                    drawing = False
            elif event.type == pygame.MOUSEMOTION:
                # Mouse Hover effect
                tools_menu.hover_tool(mouse_x, mouse_y)

                # Only append the data if the mouse is within the paint surface
                if paint_surface_collision(
                    mouse_x,
                    mouse_y,
                    paint_surface_offset_x,
                    paint_surface_offset_y,
                    paint_surface_width,
                    paint_surface_height,
                ):
                    if drawing:
                        # Pencil
                        tool.get_pencil().append(
                            paint_mouse_x, paint_mouse_y, drawn_history, current_layer
                        )
                        # Pen
                        tool.get_pen().append(
                            paint_mouse_x,
                            paint_mouse_y,
                            convert_string_to_int(selected_size),
                            selected_color,
                            drawn_history,
                            current_layer,
                        )
                        # Eraser
                        tool.get_eraser().append(
                            paint_mouse_x,
                            paint_mouse_y,
                            convert_string_to_int(selected_size),
                            drawn_history,
                            current_layer,
                        )
                        # Rectangle
                        tool.get_rectangle().append(
                            paint_mouse_x,
                            paint_mouse_y,
                            convert_string_to_int(selected_size),
                            selected_color,
                            drawn_history,
                            current_layer,
                        )
                        # Circle
                        tool.get_circle().append(
                            paint_mouse_x,
                            paint_mouse_y,
                            convert_string_to_int(selected_size),
                            selected_color,
                            drawn_history,
                            current_layer,
                        )

        # ! Update the display
        pygame.display.flip()

    # ! Quit Pygame
    pygame.quit()
    sys.exit()


# Update paint surface
def paint_surface_update(
    width: int,
    height: int,
    color: tuple,
    tools_menu_offset_x: int,
    tools_menu_offset_y: int,
):
    global DEFAULT_main_surface_WIDTH
    global DEFAULT_main_surface_HEIGHT
    global paint_surface
    global paint_surface_width
    global paint_surface_height

    # Convert the width and height to integers
    width = convert_string_to_int(width)
    height = convert_string_to_int(height)
    global size_color_field_offset_x

    if (
        width == paint_surface_width and height == paint_surface_height
    ):  # If the width and height are the same, do not update the paint surface
        return
    if (
        width <= 0 or height <= 0
    ):  # If the width and height are less than 0, do not update the paint surface
        return
    if (
        width
        > DEFAULT_main_surface_WIDTH
        - paint_surface_offset_x
        - tools_menu_offset_x
        - size_color_field_offset_x
        or height
        > DEFAULT_main_surface_HEIGHT - paint_surface_offset_y - tools_menu_offset_y
    ):  # If the width and height are greater than the main surface minus menu offset & tools menu offset, do not update the paint surface
        return

    paint_surface_width = width
    paint_surface_height = height
    paint_surface = pygame.Surface((paint_surface_width, paint_surface_height))
    paint_surface.fill(color)


# Clear paint surface
def clear_imported_image():
    # Get global variable
    global imported_image

    # Clear image from surface
    imported_image = None


# Check if mouse is within the paint surface
def paint_surface_collision(
    mouse_x: int,
    mouse_y,
    paint_surface_offset_x: int,
    paint_surface_offset_y: int,
    paint_surface_width: int,
    paint_surface_height: int,
):
    if (
        mouse_x > paint_surface_offset_x
        and mouse_x < paint_surface_offset_x + paint_surface_width
    ):
        if (
            mouse_y > paint_surface_offset_y
            and mouse_y < paint_surface_offset_y + paint_surface_height
        ):
            return True
    return False


def convert_string_to_int(string):
    try:
        if string:
            return int(string)
        else:
            return 0  # Default value for empty string
    except ValueError:
        # Handle the ValueError if the string cannot be converted to an integer
        print("Error: The string is not a valid integer.")
        return 0  # Return a default value in case of an error


def convert_int_to_string(integer):
    return str(integer)


def is_valid_size(size):
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


def is_valid_hex_color(hex_color):
    # Regular expression for a 24-bit color code in hexadecimal format
    hex_color_pattern = re.compile(r"^#([0-9a-fA-F]{6})$")

    # Check if the input string matches the pattern
    match = hex_color_pattern.match(hex_color)

    # Return True if there is a match, otherwise False
    return bool(match)


if __name__ == "__main__":
    # Call main function
    main()
