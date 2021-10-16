import turtle 
import random

from pythonds3 import Stack

WIDTH = 1024
HEIGHT = 1024

def move_tower(height, from_pole, to_pole, with_pole):
    if height >= 1:
        move_tower(height - 1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height - 1, with_pole, to_pole, from_pole)

def move_disk(from_p, to_p):
    print("moving disk from", from_p, "to", to_p)

def main():
    turtle.setup(WIDTH, HEIGHT)
    turtle.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    turtle.colormode(255)

    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    t3 = turtle.Turtle()
    
    p1 = turtle.Turtle()
    p2 = turtle.Turtle()
    p3 = turtle.Turtle()

    for i, p in enumerate([p1, p2, p3]):
        p.shape("square")
        p.turtlesize(HEIGHT // 30, 1, None)
        p.penup()
        p.setposition((WIDTH // 3) * i + WIDTH // 6, 10)

    for i, t in enumerate([t1, t2, t3]):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        t.shape("square")
        t.color(*color)
        t.turtlesize(1, i * (WIDTH // 300) + (WIDTH // 1000))
        t.penup()
        t.setpos(WIDTH // 6, 10 - i)

    turtle.exitonclick()

if __name__ == "__main__":
    main()