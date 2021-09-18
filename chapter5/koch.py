import turtle

WIDTH = 1024
HEIGHT = 1024

def koch(t, order, step):
    if order == 0:
        t.forward(step)
    else:
        koch(t, order - 1, step // 3)
        t.left(60)
        koch(t, order - 1, step // 3)
        t.right(120)
        koch(t, order - 1, step // 3)
        t.left(60)
        koch(t, order - 1, step // 3)


def main():
    t = turtle.Turtle()
    s = turtle.Screen()
    
    s.setup(WIDTH, HEIGHT)
    turtle.setworldcoordinates(0, 0, WIDTH, HEIGHT)

    t.penup()
    t.goto((WIDTH // 3, HEIGHT // 3))
    t.down()

    order = 2
    step = (WIDTH // 3) // order

    # t.speed("slowest")

    koch(t, order, step)

    s.exitonclick()

if __name__ == "__main__":
    main()