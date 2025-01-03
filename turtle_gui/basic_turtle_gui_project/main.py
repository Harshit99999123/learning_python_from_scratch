from turtle import Turtle, Screen
from polygon import Polygon

turtle = Turtle()
for i in range(3, 11):
    polygon = Polygon(i)
    polygon.draw_figure(turtle)

screen = Screen()
screen.exitonclick()
