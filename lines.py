from turtle import Turtle


class Lines(Turtle):

    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.hideturtle()
        self.pensize(5)

    def draw_lines(self):
        y_loc = -260
        loop = 1
        while loop < 15:
            self.penup()
            self.goto(-300, y_loc)
            self.pendown()
            for _ in range(15):
                self.forward(15)
                self.penup()
                self.forward(30)
                self.pendown()
            y_loc += 40
            loop += 1
