import turtle

WIDTH = 1024
HEIGHT = 1024

def koch_curve(t, order, step):
    if order == 0:
        t.forward(step)
    elif order > 0:
        koch_curve(t, order - 1, step // 3)
        t.right(60)
        koch_curve(t, order - 1, step // 3)
        t.left(120)
        koch_curve(t, order - 1, step // 3)
        t.right(60)
        koch_curve(t, order - 1, step // 3)
    else:
        pass


def koch_snowflake(t, order, step):
    for i in range(3):
        koch_curve(t, order, step)
        t.left(120)


def main():
    t = turtle.Turtle()
    s = turtle.Screen()
    
    s.setup(WIDTH, HEIGHT)
    turtle.setworldcoordinates(0, 0, WIDTH, HEIGHT)

    order = 0
    step = (WIDTH // 2) // (order + 2)

    t.penup()
    t.goto(((WIDTH // 2) // (order * 2 + 1), (HEIGHT // 2)))
    t.down()

    koch_snowflake(t, order, step)

    s.exitonclick()

if __name__ == "__main__":
    main()