from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        super().color("blue")
        super().shape("square")
        super().penup()
        super().speed("fastest")
        self.shapesize(3,0.5)
        super().goto(370,0)
    def up(self):
        if super().ycor()+20 < 290:
            super().goto(super().xcor(),super().ycor()+30)
    def down(self):
        if super().ycor() + -20 > -290:
            super().goto(super().xcor(), super().ycor()-30)



