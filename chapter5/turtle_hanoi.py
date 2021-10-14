import turtle 

from pythonds3 import Stack

SCREEN_WIDTH = 2048
SCREEN_HEIGHT = 2048
HEIGHT = 3
TURTLE_HEIGHT = 10

def move_tower(height, from_pole, to_pole, with_pole):
    if height >= 1:
        move_tower(height - 1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height - 1, with_pole, to_pole, from_pole)

def move_disk(from_p, to_p):
    print("moving disk from", from_p, "to", to_p)

def main():
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    t3 = turtle.Turtle()
    
    turtle.exitonclick()

if __name__ == "__main__":
    main()