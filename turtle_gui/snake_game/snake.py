from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVEMENT_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        for position in STARTING_POSITIONS:
            self.add_segment(position)
        self.head = self.segments[0]

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            current_segment = self.segments[seg_num]
            current_segment.goto((new_x, new_y))
        self.head.forward(MOVEMENT_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
            self.move()

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
            self.move()

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
            self.move()

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
            self.move()
