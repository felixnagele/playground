# Paint2D 🎨

## Description

Paint2D is a Python-based 2D painting application crafted with Pygame. The main class serves as the central hub for drawing components and event handling, integrating seamlessly with a menu class for organized user interaction.

## Features

### Menu Tools

A dedicated class provides an intuitive selection menu for tools like fill, clear, pencil, pen, eraser, rectangle, and circle.

Each tool is encapsulated in its own class, ensuring modular and efficient implementation.

The suite of tools includes:

- Fill: Fills a designated area with color.
- Clear: Clears the entire screen.
- Pencil: Draws in black with a fixed size of 1.
- Pen: Allows users to draw in a customizable color and size.
- Eraser: Erases drawn elements with an adjustable size.
- Rectangle: Draws outlined rectangles with specified color and size.
- Circle: Draws outlined circles with specified color and size.

### Paint Layers

Utilizing a paint history dictionary organized into layers, Paint2D ensures ordered tool application for a visually coherent output.

### Advanced Functionality

- Resizable Window: Paint2D features a resizable window for adaptable workspace.
- Customizable Paint Surface: Users can set paint surface dimensions, respecting screen size limitations.
- Image Import/Export: Supports PNG image import and export for expanded creative possibilities.

Project inspired by the professional and free paint program: [PAINT.NET](https://www.getpaint.net/)

## Dependencies

How to install pygame?

```bash
pip install pygame
```

## Usage

To run the Paint2D application, execute the following command in your terminal:

```bash
python main.py
```
