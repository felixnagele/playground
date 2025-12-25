# Tools Menu
import pygame
from tool import Tool


class ToolsMenu:
    window_width = None
    window_height = None
    main_surface = None
    paint_surface = None
    obj_width = 32
    obj_height = 32
    obj_gap = 50
    offset_x = 125
    offset_y = 20
    border = 1
    tool_item_list = []
    tool_image_list = []
    tool_image_hover_list = []
    tool_item_width = 32
    tool_item_height = 32
    tool_item_gap = 64
    tool_item_x = []
    tool_item_y = []
    tool_item_active = None
    tool_item_selected = None
    tool_item_hover = None
    size_field_location_list = []
    color_field_location_list = []
    selected_tool_location_list = []
    size_field_width = 35
    size_field_height = 35
    color_field_width = 90
    color_field_height = 35

    def __init__(
        self,
        window_width: int,
        window_height: int,
        main_surface: pygame.Surface,
        paint_surface: pygame.Surface,
    ):
        self.window_width = window_width
        self.window_height = window_height
        self.main_surface = main_surface
        self.paint_surface = paint_surface
        tool = Tool()
        self.tool_item_list = tool.get_tool_item_list()
        self.tool_image_list = tool.get_tool_image_list()
        self.tool_image_hover_list = tool.get_tool_image_hover_list()
        self.tool_item_active = dict.fromkeys(
            self.tool_item_list, False
        )  # Convert list to dict with all values on False
        self.tool_item_selected = dict.fromkeys(
            self.tool_item_list, False
        )  # Convert list to dict with all values on False
        self.tool_item_hover = dict.fromkeys(
            self.tool_item_list, False
        )  # Convert list to dict with all values on False
        self.calculate_tool_coordinates()

    def __str__(self) -> str:
        return f"ToolsMenu: window_width={self.window_width}, window_height={self.window_height}"

    def update_window(self, window_width, window_height, main_surface, paint_surface):
        self.window_width = window_width
        self.window_height = window_height
        self.main_surface = main_surface
        self.paint_surface = paint_surface
        self.calculate_tool_coordinates()

    def update(self, main_surface, paint_surface):
        self.main_surface = main_surface
        self.paint_surface = paint_surface

    def calculate_tool_coordinates(self):
        for i in range(len(self.tool_item_list)):
            self.tool_item_x.insert(
                i, self.window_width - self.tool_item_width - self.tool_item_gap
            )
            self.tool_item_y.insert(
                i,
                self.window_height
                - self.tool_item_height
                - self.tool_item_gap * (i + 1),
            )

    # Draw the tool items from the tools_item_list and use the images of the tools_image_list
    def draw(self, pygame: pygame):
        for i in range(len(self.tool_item_list)):
            image = pygame.image.load(self.tool_image_list[i])
            image = pygame.transform.scale(
                image, (self.tool_item_width, self.tool_item_height)
            )
            self.main_surface.blit(image, (self.tool_item_x[i], self.tool_item_y[i]))

    def draw_selected_tool(self, pygame: pygame):
        for i in range(len(self.tool_item_list)):
            if self.tool_item_selected[self.tool_item_list[i]]:
                image = pygame.image.load(self.tool_image_hover_list[i])
                image = pygame.transform.scale(
                    image, (self.tool_item_width, self.tool_item_height)
                )
                self.main_surface.blit(
                    image,
                    (
                        self.get_selected_tool_location()[0],
                        self.get_selected_tool_location()[1],
                    ),
                )

    def draw_hover_tool(self, pygame: pygame):
        for i in range(len(self.tool_item_list)):
            if self.tool_item_hover[self.tool_item_list[i]]:
                # pygame.draw.rect(self.main_surface, (255,0,0), (300, 300, 50, 50))
                image = pygame.image.load(self.tool_image_hover_list[i])
                image = pygame.transform.scale(
                    image, (self.tool_item_width, self.tool_item_height)
                )
                self.main_surface.blit(
                    image, (self.tool_item_x[i], self.tool_item_y[i])
                )

    def draw_size_color_fields(self, pygame: pygame):
        gap_text_y = 7
        gap_text_x = 5
        pygame.draw.rect(
            self.main_surface,
            (0, 0, 0),
            (
                self.get_size_field_location()[0] - gap_text_x,
                self.get_size_field_location()[1]
                - self.size_field_height // 2
                + gap_text_y,
                self.size_field_width,
                self.size_field_height,
            ),
            self.border,
        )
        pygame.draw.rect(
            self.main_surface,
            (0, 0, 0),
            (
                self.get_color_field_location()[0] - gap_text_x,
                self.get_color_field_location()[1]
                - self.color_field_height // 2
                + gap_text_y,
                self.color_field_width,
                self.color_field_height,
            ),
            self.border,
        )

    # Collision detection for the tool items
    def collision(self, mouse_x: int, mouse_y: int):
        for i in range(len(self.tool_item_list)):
            if (
                mouse_x >= self.tool_item_x[i]
                and mouse_x <= self.tool_item_x[i] + self.tool_item_width
                and mouse_y >= self.tool_item_y[i]
                and mouse_y <= self.tool_item_y[i] + self.tool_item_height
            ):
                self.tool_item_active[self.tool_item_list[i]] = True
                print(f"Collision: {self.tool_item_list[i]}")
                # Reset all selected states -> Set all to False
                for j in range(len(self.tool_item_list)):
                    self.tool_item_selected[self.tool_item_list[j]] = False
                # Select current item -> Set the one to True
                self.tool_item_selected[self.tool_item_list[i]] = True

    def collision_size_field(self, mouse_x: int, mouse_y: int) -> bool:
        size_x = self.get_size_field_location()[0]
        size_y = self.get_size_field_location()[1]

        if (
            mouse_x >= size_x
            and mouse_x <= size_x + self.size_field_width
            and mouse_y >= size_y
            and mouse_y <= size_y + self.size_field_height
        ):
            return True
        return False

    def collision_color_field(self, mouse_x: int, mouse_y: int) -> bool:
        color_x = self.get_color_field_location()[0]
        color_y = self.get_color_field_location()[1]

        if (
            mouse_x >= color_x
            and mouse_x <= color_x + self.color_field_width
            and mouse_y >= color_y
            and mouse_y <= color_y + self.color_field_height
        ):
            return True
        return False

    def hover_tool(self, mouse_x: int, mouse_y: int):
        for i in range(len(self.tool_item_list)):
            if (
                mouse_x >= self.tool_item_x[i]
                and mouse_x <= self.tool_item_x[i] + self.tool_item_width
                and mouse_y >= self.tool_item_y[i]
                and mouse_y <= self.tool_item_y[i] + self.tool_item_height
            ):
                # Hover current item -> Set the one to True
                self.tool_item_hover[self.tool_item_list[i]] = True
                # Reset all other tool states except the one hovered -> Set all except one to False
                hover_key = self.tool_item_list[i]
                for j in range(len(self.tool_item_list)):
                    if hover_key != self.tool_item_list[j]:
                        self.tool_item_hover[self.tool_item_list[j]] = False
                    else:
                        self.tool_item_hover[self.tool_item_list[j]] = True
            else:
                self.tool_item_hover[self.tool_item_list[i]] = False

    # Calculate Coordinates for size input field
    def get_size_field_location(self):
        position = len(self.tool_item_list) + 1
        field_gap = 75
        self.size_field_location_list.insert(
            0, self.window_width - self.tool_item_width - self.tool_item_gap - field_gap
        )
        self.size_field_location_list.insert(
            1,
            self.window_height - self.tool_item_height - self.tool_item_gap * position,
        )
        return self.size_field_location_list

    # Calculate Coordinates for color input field
    def get_color_field_location(self):
        position = len(self.tool_item_list) + 1
        field_gap = 30
        self.color_field_location_list.insert(
            0, self.window_width - self.tool_item_width - self.tool_item_gap - field_gap
        )
        self.color_field_location_list.insert(
            1,
            self.window_height - self.tool_item_height - self.tool_item_gap * position,
        )
        return self.color_field_location_list

    def get_selected_tool_location(self):
        position = len(self.tool_item_list) + 2
        self.selected_tool_location_list.insert(
            0, self.window_width - self.tool_item_width - self.tool_item_gap
        )
        self.selected_tool_location_list.insert(
            1,
            self.window_height - self.tool_item_height - self.tool_item_gap * position,
        )
        return self.selected_tool_location_list

    # Getters
    def get_offset_x(self):
        return self.offset_x

    def get_offset_y(self):
        return self.offset_y

    def get_tool_item_active(self):
        return self.tool_item_active

    def get_tool_item_list(self):
        return self.tool_item_list

    def get_tool_image_list(self):
        return self.tool_image_list
