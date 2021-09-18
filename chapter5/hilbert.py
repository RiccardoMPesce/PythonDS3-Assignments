import turtle

WIDTH = 1024
HEIGHT = 1024

def hilbert(t, order, direction, step):
    print(f"Calling hilbert with order {order}, direction {direction}, step {step}.")
    if order > 0:
        t.left(direction * 90)
        hilbert(t, order - 1, - direction, step)
        t.forward(step)
        t.right(direction * 90)
        hilbert(t, order - 1, direction, step)
        t.forward(step)
        hilbert(t, order - 1, direction, step)
        t.right(direction * 90)
        t.forward(step)
        hilbert(t, order - 1, - direction, step)
        t.left(direction * 90)


def main():
    t = turtle.Turtle()
    s = turtle.Screen()
    
    s.setup(WIDTH, HEIGHT)
    turtle.setworldcoordinates(0, 0, WIDTH, HEIGHT)

    t.penup()
    t.goto((WIDTH // 10, HEIGHT // 10))
    t.down()

    order = 2

    t.speed("fastest")

    hilbert(t, order, 1, (WIDTH // 5) // order)

    s.exitonclick()


if __name__ == "__main__":
    main()