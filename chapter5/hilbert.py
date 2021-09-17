import turtle

WIDTH = 1024
HEIGHT = 1024
ORDER = 3
LEN = WIDTH // 2

def hilbert(order, t, angle=90, step=WIDTH // 2):
    pass
    

def main():
    t = turtle.Turtle()
    s = turtle.Screen()
    
    s.setup(WIDTH, HEIGHT)
    turtle.setworldcoordinates(0, 0, WIDTH, HEIGHT)

    t.penup()
    t.goto((WIDTH // 4, HEIGHT // 4))
    t.down()

    hilbert(3, t)

    s.exitonclick()



if __name__ == "__main__":
    main()