import math
import turtle
import random

def tree(branch_len, t):
    t.pensize(branch_len ** (1 / 2))
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - random.randint(0, branch_len), t)
        t.left(40)
        tree(branch_len - random.randint(0, branch_len), t)
        t.right(20)
        t.backward(branch_len)

def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(150, t)
    my_win.exitonclick()

if __name__ == "__main__":
    main()