import turtle
from turtle import Turtle, Screen
import random
pen = Turtle()
pen.hideturtle()
pen.penup()
pen.goto(-100, 0)
raceend = False
super1 = Turtle()
super2 = Turtle()
super3 = Turtle()
super2.shape("turtle")
super1.shape("turtle")
super3.shape("turtle")
screen = Screen()
screen.setup(600, 500)
screen.title("Bet Game ")
super1.color("green")
super1.penup()
super1.goto(x=-280, y=0)
super2.color("red")
super2.penup()
super2.goto(x=-280, y=30)
super3.color("blue")
super3.penup()
super3.goto(x=-280, y=-30)
bet = screen.textinput("Make a bet ", "Which turtle will win the race, choose a color green blue red: ")
bet2 = screen.textinput("Make a bet", "Which turtle will win the race, choose a color green blue red: ")
list = [super1, super2, super3]
random.shuffle(list)
while not raceend:
    for n in list:
        n.forward(random.randint(0, 25))
        if n.xcor() >= 290:
            pen.write(f"The {n.color()[0]} one win", font=("Calibri", 20, "bold"))
            if bet == n.color()[0]:
                pen.goto(-100, -30)
                pen.write(f"The first person win", font=("Calibri", 20, "bold"))
            elif bet2 == n.color()[0]:
                pen.goto(-100, -30)
                pen.write(f"The second person win", font=("Calibri", 20, "bold"))
            else:
                pen.goto(-100, -30)
                pen.write(f"You both lost", font=("Calibri", 20, "bold"))

            raceend = True
            break

screen.exitonclick()
