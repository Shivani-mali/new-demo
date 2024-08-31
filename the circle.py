import turtle
import colorsys

turtle.speed(0)
turtle.bgcolor("black")
h = 0

# Loop to create the pattern
for i in range(16):
    for j in range(18):
        c = colorsys.hsv_to_rgb(h, 1, 1)  # Smooth color transitions
        turtle.color(c)
        h += 0.008  # Slightly faster hue change for vivid colors
        
        turtle.right(90)  # Right turn
        turtle.circle(150 - j * 5, 90)  # Smaller decrement for tighter design
        turtle.left(90)  # Left turn
        turtle.circle(150 - j * 5, 90)  # Consistent size
        
        turtle.right(180)  # Back turn
        turtle.circle(30, 24)  # Slightly smaller inner circle for balance

turtle.done()
