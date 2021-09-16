import turtle
wn = turtle.Screen()
wn.setup(1000, 1000)
pen = turtle.Turtle()
wn.tracer(0, 0)
pen.up()
pen.goto(0, 0)
pen.down()


def draw(size, counter):
    if counter == 0:
        pass
    else:
        if size <= 10:
            pen.forward(size / 3)
            pen.left(60)
            pen.forward(size / 3)
            pen.right(120)
            pen.forward(size / 3)
            pen.left(60)
            pen.forward(size / 3)
        else:
            draw(size / 3, counter-1)
            pen.left(60)
            draw(size / 3, counter-1)
            pen.right(120)
            draw(size / 3, counter-1)
            pen.left(60)
            draw(size / 3, counter-1)


for i in range(3):
    draw(1000, 100)
    pen.right(120)

""""
def draw(size):
    inner_draw(size / 3)
    pen.left(60)
    inner_draw(size / 3)
    pen.right(120)
    inner_draw(size / 3)
    pen.left(60)
    inner_draw(size / 3)


def inner_draw(size):
    inner_inner_draw(size / 3)
    pen.left(60)
    inner_inner_draw(size / 3)
    pen.right(120)
    inner_inner_draw(size / 3)
    pen.left(60)
    inner_inner_draw(size / 3)


def inner_inner_draw(size):
    pen.forward(size / 3)
    pen.left(60)
    pen.forward(size / 3)
    pen.right(120)
    pen.forward(size / 3)
    pen.left(60)
    pen.forward(size / 3)
"""

turtle.update()
turtle.mainloop()
