from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(-40, 270)
        self.color("white")
        self.hideturtle()

    def increase_score(self):
        self.score += 1

    def display_score(self):
        self.write(f"Score: {self.score}", font=FONT, align=ALIGNMENT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=FONT, align=ALIGNMENT)
