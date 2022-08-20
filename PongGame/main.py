from turtle import Screen
from Player import Player
from Ball import Ball
from ScoreBoard import ScoreBoard
import time

screen = Screen()
screen.tracer(0)
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("IoI")
scoreboard = ScoreBoard()
player1 = Player()
player2 = Player()
player2.goto(-370, 0)
player2.color("green")
fscore = screen.numinput("For what", "Enter a number: ")
ball = Ball()

screen.update()
screen.listen()
screen.onkeypress(player1.up, "Up")
screen.onkeypress(player1.down, "Down")
screen.onkeypress(player2.up, "w")
screen.onkeypress(player2.down, "s")

gameon = True
while gameon:
    time.sleep(0.01)
    ball.moving()
    screen.update()
    if scoreboard.p1_score == fscore or scoreboard.p2_score == fscore:
        scoreboard.score=fscore
        scoreboard.endr()
        ball.hideturtle()
        screen.update()
        gameon = False
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce()
    if ball.distance(player1) <= 28 and ball.xcor() > 365 and ball.xcor() < 375:
        ball.bounce2()
    if ball.distance(player2) <= 28 and ball.xcor() < -365 and ball.xcor() > -375:
        ball.bounce2()
    if ball.xcor() > 395:
        ball.resetr()
        scoreboard.p2_score += 1
        scoreboard.writer()
    if ball.xcor() < -395:
        ball.resetr()
        scoreboard.p1_score += 1
        scoreboard.writer()

screen.exitonclick()
