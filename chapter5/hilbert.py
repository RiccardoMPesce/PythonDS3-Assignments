import turtle

WIDTH = 1024
HEIGHT = 1024
ORDER = 3
LEN = WIDTH // 2

def hilbert(order, t):
    if order == 1:
        draw_curve(t) 
    else:
        hilbert(order - 1)
        hilbert(order - 1)
        hilbert(order - 1)

def draw_curve(t, start=None, l=WIDTH//2, rot=None):
    if start is not None:
        t.goto(start)
    
    if rot is None:
        t.seth(90)
        t.forward(l)
        t.right(90)
        t.forward(l)
        t.right(90)
        t.forward(l)
    elif rot.lower() in ["l", "left"]:
        t.seth(180)
        t.forward(l)
        t.right(90)
        t.forward(l)
        t.right(90)
        t.forward(l)
    elif rot.lower() in ["r", "right"]:
        t.seth(0)
        t.forward(l)
        t.left(90)
        t.forward(l)
        t.left(90)
        t.forward(l)

def main():
    t = turtle.Turtle()
    s = turtle.Screen()
    
    s.setup(WIDTH, HEIGHT)
    turtle.setworldcoordinates(0, 0, WIDTH, HEIGHT)

    t.penup()
    t.goto((WIDTH // 4, HEIGHT // 4))
    t.down()

    draw_curve(t, (WIDTH // 4, HEIGHT // 4), WIDTH // 50, rot="r")
    draw_curve(t, l=WIDTH // 50, rot="l")

    s.exitonclick()



if __name__ == "__main__":
    main()