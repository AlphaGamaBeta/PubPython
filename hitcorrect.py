from turtle import Turtle, Screen
import random

game = True
pen = Turtle()
pen.hideturtle()
pen.penup()
pen.goto(-120, 0)
pen.pencolor("red")
screen = Screen()
screen.title("Scary")
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)
bomb = Turtle()
bomb.shape("square")
bomb.color("black")
bomb.penup()
bomb.goto(random.randint(-280, 280), random.randint(-280, 280))
bomb_pos = bomb.pos()
win = Turtle()
win.shape("square")
win.color("black")
win.penup()
win.goto(random.randint(-280, 280), random.randint(-280, 280))
win_pos = win.pos()
snake = Turtle()
snake.shape("square")
snake.color("white")
snake.penup()
screen.update()


def move_f():
    snake.forward(30)
    screen.update()
    if snake.xcor() >= bomb_pos[0] - 20 and snake.xcor() <= bomb_pos[0] + 20 and snake.ycor() >= bomb_pos[
        1] - 20 and snake.ycor() <= bomb_pos[1] + 20:
        pen.write(f"You  lost you hit a bomb", font=("Calibri", 20, "bold"))
    elif snake.xcor() >= win_pos[0] - 20 and snake.xcor() <= win_pos[0] + 20 and snake.ycor() >= win_pos[
        1] - 20 and snake.ycor() <= win_pos[1] + 20:
        pen.write(f"You win you collect orb", font=("Calibri", 20, "bold"))

    screen.update()


def move_b():
    snake.forward(-30)
    screen.update()
    if snake.xcor() >= bomb_pos[0] - 20 and snake.xcor() <= bomb_pos[0] + 20 and snake.ycor() >= bomb_pos[
        1] - 20 and snake.ycor() <= bomb_pos[1] + 20:
        pen.write(f"You  lost you hit a bomb", font=("Calibri", 20, "bold"))
    elif snake.xcor() >= win_pos[0] - 20 and snake.xcor() <= win_pos[0] + 20 and snake.ycor() >= win_pos[
        1] - 20 and snake.ycor() <= win_pos[1] + 20:
        pen.write(f"You win you collect orb", font=("Calibri", 20, "bold"))
    screen.update()


def Clock():
    snake.right(30)
    screen.update()


def CClock():
    snake.right(-30)
    screen.update()
def origin():
    snake.goto(0,0)
    screen.update()
screen.listen()
screen.onkey(move_f, "w")
screen.onkey(move_b, "s")
screen.onkey(Clock, "d")
screen.onkey(CClock, "a")
screen.onkey(origin, "o")

screen.exitonclick()
