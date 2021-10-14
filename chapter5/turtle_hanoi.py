import turtle 

from pythonds3 import Stack

SCREEN_WIDTH = 2048
SCREEN_HEIGHT = 2048
HEIGHT = 3
TURTLE_HEIGHT = 10

def move_tower(height, from_pole, to_pole, with_pole):
    if from_pole.is_empty() and to_pole.is_empty() and with_pole.is_empty():
        for i in range(1, height + 1):
            from_pole.push(f"disk{i}")
    if height >= 1:
        move_tower(height - 1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        to_pole.push(from_pole.pop())
        move_tower(height - 1, with_pole, to_pole, from_pole)

def move_disk(from_p, to_p):
    print("moving disk from", from_p.name, "to", to_p.name)

def main():
    turtles = [turtle.Turtle() for _ in range(HEIGHT)] 
    floor = turtle.Turtle()
    floor.shape("square")
    print(turtles)
    turtle.exitonclick()

if __name__ == "__main__":
    main()