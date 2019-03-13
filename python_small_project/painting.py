import turtle
import inspect

def draw_square(turtle_pen):
    for i in range(4):
        turtle_pen.forward(100)
        turtle_pen.right(90)

def draw_circle(turtle_pen):
    turtle_pen.circle(100)

def draw_triangle(turtle_pen):
    for i in range(3):
        turtle_pen.right(120)
        turtle_pen.forward(100)

def draw_diamond(turtle_pen):
    for i in range(4):
        if i == 2:
            turtle_pen.right(60)
        turtle_pen.right(60)
        turtle_pen.forward(100)

def draw_pattern():
    screen = turtle.Screen()
    screen.bgcolor("red")

    # pen = turtle.RawTurtle(screen)
    pen = turtle.Turtle()
    pen.speed("slowest")
    pen.color("white","blue")
    pen.shape("turtle")
    pen.pensize(5)

    pen.begin_fill()
    #draw a square
    draw_square(pen)
    pen.end_fill()

    another_pen = turtle.Turtle()
    another_pen.color("black")
    another_pen.shape("arrow")

    #draw a circle
    draw_circle(another_pen)

    third_pen = turtle.Turtle()
    third_pen.color("yellow")
    third_pen.shape("circle")

    # draw a triangle
    draw_triangle(third_pen)

    screen.exitonclick()

def draw_square_circle():
    screen = turtle.Screen()
    screen.bgcolor("red")

    pen = turtle.Turtle()
    pen.speed("fast")
    pen.color("yellow")
    pen.shape("turtle")
    pen.pensize(3)

    for i in range(36):
        draw_square(pen)
        pen.right(10)

    screen.exitonclick()

def draw_triangle_flower():
    screen = turtle.Screen()

    pen = turtle.Turtle()
    pen.speed("fast")
    pen.color("blue")
    pen.shape("turtle")
    pen.pensize(3)

    # draw_diamond(pen)
    for i in range(36):
        draw_diamond(pen)
        pen.right(10)
    pen.right(90)
    pen.forward(300)

    screen.exitonclick()

#draw_pattern()
# draw_square_circle()
draw_triangle_flower()


#the way to see source code
# import inspect
# lines = inspect.getsource(turtle)
# print(lines)