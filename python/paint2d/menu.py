# Menu
import pygame


class Menu:
    main_surface = None
    paint_surface = None
    menu_item_list = ["Import", "Export", "Dimension", "X", "Y", "MX", "MY"]
    width = 120
    height = 40
    menu_item_x_start = 20
    menu_item_y_start = 20
    menu_item_gap = 20
    menu_item_x = []
    menu_item_y = []
    menu_color_status = [(52, 152, 219), (240, 240, 240)]  # default, #textfield
    menu_color_pointer = 0
    menu_color_border = (0, 0, 0)
    menu_font = None
    menu_font_size = 24
    menu_font_color = (28, 40, 51)
    menu_item_active = dict.fromkeys(
        menu_item_list, False
    )  # Convert list to dict with all values on False
    menu_import_path = "src/imports/paint2d_import.png"
    menu_export_path = "src/exports/paint2d_export.png"
    menu_x_y_location_list = []
    menu_x_y_font_size = 30

    # Constructor
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
        for i in range(len(self.menu_item_list)):
            self.menu_item_x.insert(
                i, self.menu_item_x_start + self.width * i + self.menu_item_gap * i
            )
            self.menu_item_y.insert(i, self.menu_item_y_start)

    # String representation
    def __str__(self):
        return f"ExportMenu: ..."

    # Draw the import & export item
    def draw_import_export(self, pygame: pygame):
        self.menu_color_pointer = 0
        for i in range(0, 2):
            pygame.draw.rect(
                self.main_surface,
                self.menu_color_status[self.menu_color_pointer],
                (self.menu_item_x[i], self.menu_item_y[i], self.width, self.height),
            )
            font = pygame.font.Font(self.menu_font, self.menu_font_size)
            text = font.render(self.menu_item_list[i], True, self.menu_font_color)
            text_rect = text.get_rect()
            text_rect.center = (
                self.menu_item_x[i] + (self.width // 2),
                self.menu_item_y[i] + (self.height // 2),
            )
            self.main_surface.blit(text, text_rect)

    # Draw the dimension item
    def draw_dimension(self, pygame: pygame):
        # Dimension Item
        index = 2
        self.menu_color_pointer = 0
        pygame.draw.rect(
            self.main_surface,
            self.menu_color_status[self.menu_color_pointer],
            (self.menu_item_x[index], self.menu_item_y[index], self.width, self.height),
        )
        font = pygame.font.Font(self.menu_font, self.menu_font_size)
        text = font.render(self.menu_item_list[index], True, self.menu_font_color)
        text_rect = text.get_rect()
        text_rect.center = (
            self.menu_item_x[index] + (self.width // 2),
            self.menu_item_y[index] + (self.height // 2),
        )
        self.main_surface.blit(text, text_rect)

        # X, Y Item
        self.menu_color_pointer = 1
        for i in range(3, 5):
            pygame.draw.rect(
                self.main_surface,
                self.menu_color_status[self.menu_color_pointer],
                (self.menu_item_x[i], self.menu_item_y[i], self.width, self.height),
            )  # Content
            pygame.draw.rect(
                self.main_surface,
                self.menu_color_border,
                (self.menu_item_x[i], self.menu_item_y[i], self.width, self.height),
                3,
            )  # Border
            font = pygame.font.Font(self.menu_font, self.menu_font_size)
            text = font.render(self.menu_item_list[i], True, self.menu_font_color)
            text_rect = text.get_rect()
            text_rect.center = (
                self.menu_item_x[i] + (10),
                self.menu_item_y[i] + (self.height // 2),
            )
            self.main_surface.blit(text, text_rect)

    # Draw max x, y
    def draw_max_x_y(self, pygame: pygame, max_x: str, max_y: str):
        self.menu_color_pointer = 1
        for i in range(5, 7):
            pygame.draw.rect(
                self.main_surface,
                self.menu_color_status[self.menu_color_pointer],
                (self.menu_item_x[i], self.menu_item_y[i], self.width, self.height),
            )  # Content
            pygame.draw.rect(
                self.main_surface,
                self.menu_color_border,
                (self.menu_item_x[i], self.menu_item_y[i], self.width, self.height),
                3,
            )  # Border
            font = pygame.font.Font(self.menu_font, self.menu_font_size)
            text = font.render(self.menu_item_list[i], True, self.menu_font_color)
            text_rect = text.get_rect()
            text_rect.center = (
                self.menu_item_x[i] + (20),
                self.menu_item_y[i] + (self.height // 2),
            )
            self.main_surface.blit(text, text_rect)

        # Max X Text
        font = pygame.font.Font(self.menu_font, self.menu_x_y_font_size)
        text_max_x = font.render(max_x, True, self.menu_font_color)
        text_rect_max_x = text_max_x.get_rect()
        text_rect_max_x.center = (
            self.menu_item_x[5] + (70),
            self.menu_item_y[5] + (self.height // 2),
        )
        self.main_surface.blit(text_max_x, text_rect_max_x)

        # Max Y Text
        font = pygame.font.Font(self.menu_font, self.menu_x_y_font_size)
        text_max_y = font.render(max_y, True, self.menu_font_color)
        text_rect_max_y = text_max_y.get_rect()
        text_rect_max_y.center = (
            self.menu_item_x[6] + (60),
            self.menu_item_y[6] + (self.height // 2),
        )
        self.main_surface.blit(text_max_y, text_rect_max_y)

    # Import Image
    def import_image(self, pygame: pygame):
        image = pygame.image.load(self.menu_import_path)
        return image

    # Export Image
    def export_image(self, pygame: pygame):
        pygame.image.save(self.paint_surface, self.menu_export_path)

    # Collision with menu items
    def collision(self, mouse_x: int, mouse_y: int):
        for i in range(len(self.menu_item_list)):
            if (
                mouse_x > self.menu_item_x[i]
                and mouse_x < self.menu_item_x[i] + self.width
            ):
                if (
                    mouse_y > self.menu_item_y[i]
                    and mouse_y < self.menu_item_y[i] + self.height
                ):
                    self.menu_item_active[self.menu_item_list[i]] = True
                    print(self.menu_item_active)

    # Getters
    def get_menu_item_active(self):
        return self.menu_item_active

    def get_menu_item_list(self):
        return self.menu_item_list

    def get_x_y_font_size(self):
        return self.menu_x_y_font_size

    def get_x_y_location_list(self):
        self.menu_x_y_location_list.insert(
            0, self.menu_item_x[3] + (30)
        )  # X Item (X Coordinate)
        self.menu_x_y_location_list.insert(
            1, self.menu_item_y[3] + (10)
        )  # X Item (Y Coordinate)
        self.menu_x_y_location_list.insert(
            2, self.menu_item_x[4] + (30)
        )  # Y Item (X Coordinate)
        self.menu_x_y_location_list.insert(
            3, self.menu_item_y[4] + (10)
        )  # Y Item (Y Coordinate)
        return self.menu_x_y_location_list

    def window_update(
        self, main_surface: pygame.Surface, paint_surface: pygame.Surface
    ):
        self.main_surface = main_surface
        self.paint_surface = paint_surface
