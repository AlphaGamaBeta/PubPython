from turtle import Turtle
from random import choice


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        super().color("red")
        super().shape("circle")
        super().shapesize(0.5, 0.5)
        super().penup()
        self.dir = [-1, 1]
        self.n = 3 * choice(self.dir)
        self.m = 3 * choice(self.dir)

    def moving(self):
        super().goto(super().xcor() + self.m, super().ycor() + self.n)

    def bounce(self):
        self.n *= -1
        self.m = self.m - self.m / 3.9
    def bounce2(self):
        self.m = (self.m * -1) + (self.m/2 * -1)
    def resetr(self):
        super().goto(0,0)
        self.n = 3 * choice(self.dir)/1.1
        self.m= 3 * choice(self.dir)/1.1
