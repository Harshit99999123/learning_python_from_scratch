from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which color turtle will win the race? Enter a color: ")
is_race_on = False
print(user_bet)
y_positions = [-70, -40, -10, 20, 50, 80]
colors = ["red", "yellow", "orange", "blue", "green", "purple"]
all_turtle = []

for turtle_index in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[turtle_index])
    turtle.goto(-230, y_positions[turtle_index])
    all_turtle.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won. {winning_color} turtle won.")
            else:
                print(f"You lost. {winning_color} turtle won.")
            is_race_on = False
        turtle.forward(random.randint(0, 10))


screen.exitonclick()
