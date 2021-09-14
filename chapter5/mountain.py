import turtle
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

def draw_hills(points, t, level):
    color = ((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    t.color("black", color)
    p0 = points[0]
    t.up()
    t.goto(*p0)
    t.down()

    t.begin_fill()
    for pt in points:
        t.goto(*pt)

    t.goto(points[-1][0], 0)
    t.goto(*p0)

    t.end_fill()

def mountain(points, t, levels):
    draw_hills(points, t, levels)
    if levels > 0:
        new_points = [(x, abs(y - random.randint(0, y))) for (x, y) in points]
        mountain(new_points, t, levels - 1)

def main():
    t = turtle.Turtle()
    win = turtle.Screen()
    win.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    win.setworldcoordinates(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
    win.colormode(255)

    p1 = (0, 0)
    p2 = (SCREEN_WIDTH - 750, SCREEN_HEIGHT - 250)
    p3 = (SCREEN_WIDTH - 500, SCREEN_HEIGHT - 750)
    p4 = (SCREEN_WIDTH - 250, SCREEN_HEIGHT - 500)
    p5 = (SCREEN_WIDTH, 10)

    mountain([p1, p2, p3, p4, p5], t, 3)

    win.exitonclick()

if __name__ == "__main__":
    main()