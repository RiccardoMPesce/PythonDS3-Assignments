import turtle 
import random

from pythonds3 import Stack

WIDTH = 1024
HEIGHT = 1024

TOWER_HEIGHT = 3

DEFAULT_LEN = 20

class Peg:
    def __init__(self, height, color, x, y):
        self.height = height
        self._peg = []
        self.size = 0
        
        # Turtle object
        self.tower = turtle.Turtle()
        self.tower.shape("square")
        self.tower.color(color)

        self.tower.up()
        self.tower.turtlesize(height // DEFAULT_LEN, 1)
        self.tower.setpos(x, y)

    def push(self, disk):
        w, _, _ = disk.disk.shapesize()
        xpos = self.tower.pos()[0]
        ypos = self.size * 25 + 10

        disk.jump_to(xpos, ypos, self.height)

        self._peg.append(disk)
        self.size += 1

    def pop(self):
        self.size -= 1
        return self._peg.pop()


class Disk:
    def __init__(self, border_color, color, width, x, y):
        self.width = width
        self.disk = turtle.Turtle()
        self.disk.shape("square")
        self.disk.turtlesize(1, width // DEFAULT_LEN)
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

        self.height = n_disks

        self.tower_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.disk_border_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.disk_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        w, h = turtle.screensize()

        peg_height = (n_disks * (DEFAULT_LEN + 5)) + (h // n_disks) * 2
        peg_distance_coeff = w // n_pegs
        peg_distance_int = peg_distance_coeff // 2
        self._pegs = [Peg(peg_height, self.tower_color, peg_distance_coeff * i + peg_distance_int, 0) for i in range(n_pegs)]        
        
        disk_w_coeff = peg_distance_int // 2
        self._disks = [Disk(self.disk_border_color, self.disk_color, disk_w_coeff * (n_disks - i), peg_distance_int, 25 * i + (h // 1.5)) for i in range(n_disks)]


    def move_tower(self, height, from_pole, to_pole, with_pole):
        if height >= 1:
            self.move_tower(height - 1, from_pole, with_pole, to_pole)
            self.move_disk(from_pole, to_pole)
            self.move_tower(height - 1, with_pole, to_pole, from_pole)

    def move_disk(self, from_p, to_p):
        print("moving disk from", from_p, "to", to_p)
        to_p.push(from_p.pop())

    def play(self):
        p1, p2, p3 = self._pegs
        for d in self._disks:
            p1.push(d)
        self.move_tower(self.n_disks, p1, p2, p3)

def main():
    turtle.setup(WIDTH, HEIGHT)
    turtle.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    turtle.colormode(255)

    sim = Simulate()
    sim.play()

    turtle.exitonclick()

if __name__ == "__main__":
    main()