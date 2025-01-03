import turtle as t
import random


def get_random_color():
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)
    random_color = (red, blue, green)
    return random_color


t.colormode(255)
turtle = t.Turtle()
turtle.speed("fastest")
for i in range(0, 360, 5):
    turtle.color(get_random_color())
    turtle.right(i)
    turtle.circle(100)
    print(turtle.position())
screen = t.Screen()
screen.exitonclick()
