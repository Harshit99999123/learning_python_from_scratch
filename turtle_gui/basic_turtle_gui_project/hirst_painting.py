import turtle as t
import random


def draw_dots():
    for i in range(0, 10):
        turtle.pendown()
        turtle.dot(20, get_random_color())
        if i != 9:
            turtle.penup()
            turtle.forward(50)


def turn_and_move_north():
    turtle.penup()
    turtle.setheading(90)
    turtle.forward(50)


def turn_and_move_east():
    turtle.setheading(0)
    draw_dots()


def turn_and_move_west():
    turtle.setheading(180)
    draw_dots()


def get_random_color():
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)
    random_color = (red, blue, green)
    return random_color


t.colormode(255)
turtle = t.Turtle()
turtle.penup()
turtle.setheading(225)
turtle.forward(300)
turtle.pendown()

next_direction = "east"

for i in range(0, 10):
    if next_direction == "east":
        turn_and_move_east()
        next_direction = "west"
    else:
        turn_and_move_west()
        next_direction = "east"
    if i != 9:
        turn_and_move_north()

turtle.hideturtle()

screen = t.Screen()
screen.exitonclick()
