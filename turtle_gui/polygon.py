class Polygon:
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides
        self.interior_angle = (360/number_of_sides)

    def draw_figure(self, turtle):
        for i in range(0, self.number_of_sides):
            turtle.forward(100)
            turtle.right(self.interior_angle)

