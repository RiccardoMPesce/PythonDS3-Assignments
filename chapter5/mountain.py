import turtle
import random

def draw_triangle(origin, color, t, wanted_hills=10):
    if origin[0] < 100 and origin[1] < 100:
        t.color("black", color)
        t.up()
        t.goto(origin[0], origin[1])
        t.down()
        t.begin_fill()
        height = random.randint(1, 100)
        width = origin[0] + 100 // wanted_hills
        t.goto(width // 2, height)
        t.goto(width, 0)
        # t.goto(origin[0], origin[1])
        t.end_fill()
        draw_triangle(t.pos(), color, t)

my_points = [[-180, -150], [0, 150], [180, -150]]
t = turtle.Turtle()
win = turtle.Screen()
win.screensize(100, 100)
win.setworldcoordinates(0, 0, 100, 100)
draw_triangle([0, 0], "brown", t)
win.exitonclick()