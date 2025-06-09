import turtle

def print_usage():
    print("""
The Q#Pixel: Pixel Art Maker V2

How to use:
1. Enter your pixel art pattern, one row at a time.
   - Use any characters to represent different colors.
   - For example, '0' for white, ':' for black, 'A' for red, etc.
2. When you finish entering the pattern, enter a blank line.
3. Then you will be prompted to assign a color to each character.
   - You can enter color names (like 'red', 'blue', 'green') or hex codes like '#ff0000'.
4. The turtle window will open and your pixel art will be drawn.

Example pattern input:
001100
110011
221122
00220

Press Enter on a blank line to finish input.

Enjoy your pixel art!
""")

def get_colors(char_set):
    """Ask the user to assign a color to each character in the pattern."""
    colors = {}
    print("Assign colors for each pixel symbol:")
    for ch in char_set:
        color = input(f"Color for '{ch}' (e.g. red, #ff0000, blue): ").strip()
        colors[ch] = color
    return colors

def draw_pixel(t, x, y, size, color):
    """Draw a filled square pixel at (x, y) with given size and color."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()

def draw_pixel_art(pattern, colors, max_canvas_size=400):
    """Draw the pixel art pattern using turtle, scaling pixel size dynamically."""
    bgc = input("Background Color: ")
    screen = turtle.Screen()
    screen.title("Q#PIXEL PYTHON TURTLE WINDOW")
    screen.bgcolor(bgc)
    
    # Disable automatic screen refresh — avoids rendering bugs
    screen.tracer(0)

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    rows = len(pattern)
    cols = max(len(row) for row in pattern)

    # Dynamically calculate pixel size to fit within max canvas size
    pixel_size_w = max_canvas_size // cols
    pixel_size_h = max_canvas_size // rows
    pixel_size = min(pixel_size_w, pixel_size_h)

    # Centering the drawing
    start_x = -cols * pixel_size / 2
    start_y = rows * pixel_size / 2

    for row_index, row in enumerate(pattern):
        for col_index, ch in enumerate(row):
            if ch in colors:
                x = start_x + col_index * pixel_size
                y = start_y - row_index * pixel_size
                draw_pixel(t, x, y, pixel_size, colors[ch])

    # Now update the screen once — prevents distortion
    screen.update()
    screen.mainloop()

def main():
    print_usage()
    print("Enter your pixel art pattern, one row per line.")
    print("Use any characters to represent colors.")
    print("Enter a blank line when done.\n")
    
    pattern = []
    while True:
        line = input()
        if line == "":
            break
        pattern.append(line)
    
    if not pattern:
        print("No pattern entered. Exiting.")
        return
    
    unique_chars = set("".join(pattern))
    colors = get_colors(unique_chars)
    draw_pixel_art(pattern, colors)

main()
