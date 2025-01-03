import turtle as t

import random

DIRECTIONS = [0, 90, 180, 270]

t.colormode(255)
turtle = t.Turtle()
turtle.pensize(15)
turtle.speed("fastest")


def get_random_color():
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)
    random_color = (red, blue, green)
    return random_color


for _ in range(0, 200):
    turtle.color(get_random_color())
    turtle.forward(30)
    turtle.setheading(random.choice(DIRECTIONS))

screen = t.Screen()
screen.exitonclick()
