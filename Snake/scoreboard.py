from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.highest_score=0
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        with open("data.txt", mode="r") as data:
            self.highest_score=int(data.read())
        self.write(f"The Score: {self.score} Highest: {self.highest_score}", align=ALIGNMENT, font=FONT)
    def reseter(self):
        if self.score > self.highest_score:
            self.highest_score=self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.highest_score))
        self.score=0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color("red")
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    def increase_scoreS(self):
        self.score += 5
        self.clear()
        self.update_scoreboard()

