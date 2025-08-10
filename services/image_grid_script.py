from PIL import Image, ImageDraw

# Input: Your container dimensions (replace with actual values)
total_width = 2560  # Example width (pixels)
total_height = 1440  # Example height (pixels)

# Grid setup (7 cols, 3 rows)
cols, rows = 5, 2

# Calculate cell width/height to fit container *and* keep 5:7 ratio
cell_width = total_width / cols
cell_height = (cell_width * 7) / 5  # Derive height from 5:7 ratio

# Check if cells fit vertically; if not, adjust width instead
if cell_height * rows > total_height:
    cell_height = total_height / rows
    cell_width = (cell_height * 5) / 7  # Derive width from 5:7 ratio

# Recalculate total dimensions (may be smaller than container due to ratio lock)
final_width = int(cell_width * cols)
final_height = int(cell_height * rows)

# Create image
img = Image.new("RGB", (final_width, final_height), "white")
draw = ImageDraw.Draw(img)

# Draw grid lines (no gaps)
for x in range(cols):
    for y in range(rows):
        left = int(x * cell_width)
        top = int(y * cell_height)
        right = int(left + cell_width)
        bottom = int(top + cell_height)
        draw.rectangle([left, top, right, bottom], outline="black", width=2)

img.save("7x3_grid_5x7_ratio.png")