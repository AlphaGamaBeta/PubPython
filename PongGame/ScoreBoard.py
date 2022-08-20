from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.p1_score=0
        self.p2_score=0
        self.writer()
        self.score=2
    def writer(self):
        self.clear()
        self.goto(240, 240)
        self.write(f"Player1: {self.p1_score}", align="center", font=("courier", 20, "normal"))
        self.goto(-240, 240)
        self.write(f"Player2: {self.p2_score}", align="center", font=("courier", 20, "normal"))
    def endr(self):
        self.goto(0, 0)
        if self.p1_score==self.score:
            self.write(f"Player 1 Wins", align="center", font=("courier", 40, "normal"))
        if self.p2_score ==self.score:
            self.write(f"Player 2 Wins", align="center", font=("courier", 40, "normal"))