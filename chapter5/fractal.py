import math
import turtle
import random

def tree(branch_len, min_step, max_step, t):
    t.color((0, 255 - branch_len if branch_len >= 0 else 255, 0))
    t.pensize(branch_len ** (1 / 2))
    a1 = random.randint(15, 45)
    a2 = random.randint(15, 45)
    step = random.randint(min_step, max_step)
    if branch_len >= min_step:
        t.forward(branch_len)
        t.right(a1)
        tree(branch_len - step, min_step, max_step, t)
        t.left(a1 + a2)
        tree(branch_len - step, min_step, max_step, t)
        t.right(a2)
        t.up()
        t.backward(branch_len)
        t.down()

def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    my_win.colormode(255)
    t.left(90)
    t.up()
    t.backward(300)
    t.down()
    tree(150, 15, 25, t)
    my_win.exitonclick()

if __name__ == "__main__":
    main()