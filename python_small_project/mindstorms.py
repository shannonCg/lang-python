import turtle

def draw_square():
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
    for i in range(4):
        pen.forward(100)
        pen.right(90)
    pen.end_fill()

    screen.exitonclick()


draw_square()