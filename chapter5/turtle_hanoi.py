import turtle 
import random

from pythonds3 import Stack

WIDTH = 1024
HEIGHT = 1024

TOWER_HEIGHT = 3

class Peg:
    def __init__(self, height, color, x, y):
        self.height = height
        self._peg = []
        self.size = 0
        
        # Turtle object
        self.tower = turtle.Turtle()
        self.tower.color(color)

        self.tower.up()
        self.tower.setpos(x, y)

    def push(self, disk):
        xpos = self.tower.pos()[0]
        ypos = self.size * 25 + 10

        disk.jump_to(xpos, ypos, self.height)

        self._peg.append(disk)

    def pop(self):
        return self._peg.pop()


class Disk:
    def __init__(self, border_color, color, x, y):
        self.disk = turtle.Turtle()
        self.disk.color(border_color, color)
        self.disk.up()
        self.disk.goto(x, y)

    def jump_to(self, x, y, h):
        self.disk.goto(self.disk.pos()[0], h)
        self.disk.goto(x, h)
        self.disk.goto(x, y)


class Simulate:
    def __init__(self, n_disks=3, n_pegs=3):
        self.n_disks = n_disks
        self.n_pegs = n_pegs

        self.tower_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.disk_border_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.disk_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        w, h = turtle.screensize()
        self._pegs = [Peg()]        
        

        

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

    

    turtle.exitonclick()

if __name__ == "__main__":
    main()