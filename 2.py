import turtle
import math

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle instance
t = turtle.Turtle()
t.speed(1)  # Set the drawing speed
t.pensize(2)  # Set the pen size

# Define functions for drawing and transforming shapes
def draw_rectangle(x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

def draw_circle(x, y, radius, color):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color(color)
    t.circle(radius)

def translate(dx, dy):
    t.penup()
    t.setx(t.xcor() + dx)
    t.sety(t.ycor() + dy)
    t.pendown()

def rotate(angle):
    t.setheading(t.heading() + angle)

def scale(sx, sy):
    t.penup()
    t.setx(t.xcor() * sx)
    t.sety(t.ycor() * sy)
    t.pendown()

# Draw and transform shapes
# Rectangle
draw_rectangle(-200, 0, 100, 50, "blue")
translate(200, 0)
draw_rectangle(0, 0, 100, 50, "blue")
rotate(45)
draw_rectangle(0, 0, 100, 50, "blue")
scale(2, 2)
draw_rectangle(0, 0, 100, 50, "blue")

# Circle
draw_circle(100, 100, 50, "red")
translate(200, 0)
draw_circle(300, 100, 50, "red")
rotate(45)
draw_circle(300, 100, 50, "red")
scale(2, 2)
draw_circle(600, 200, 50, "red")

# Keep the window open until it's closed
turtle.done()
