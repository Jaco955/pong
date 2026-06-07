import turtle
import tkinter
from tkinter import messagebox
import time

wn = turtle.Screen()
wn.title ("Rolo-Pong")
wn.bgcolor("black")
wn.setup(width=1000, height=600)
wn.tracer(0)

paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-450, 0)

paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(450, 0)


ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 6
ball.dy = 6

score_a = 0
score_b = 0

keys = {
    "w": False,
    "s": False,
    "Up": False,
    "Down": False
}

def press_w(): keys["w"] = True
def release_w(): keys["w"] = False

def press_s(): keys["s"] = True
def release_s(): keys["s"] = False

def press_Up(): keys["Up"] = True
def release_Up(): keys["Up"] = False

def press_Down(): keys["Down"] = True
def release_Down(): keys["Down"] = False

wn.listen()
wn.onkeypress(press_w, "w")
wn.onkeyrelease(release_w, "w")

wn.onkeypress(press_s, "s")
wn.onkeyrelease(release_s, "s")

wn.onkeypress(press_Up, "Up")
wn.onkeyrelease(release_Up, "Up")

wn.onkeypress(press_Down, "Down")
wn.onkeyrelease(release_Down, "Down")

def move_paddles():
    if keys["w"] and paddle_a.ycor() < 310:
        paddle_a.sety(paddle_a.ycor() + 8)
    if keys["s"] and paddle_a.ycor() > -310:
        paddle_a.sety(paddle_a.ycor() - 8)
    if keys["Up"] and paddle_b.ycor() < 310:
        paddle_b.sety(paddle_b.ycor() + 8)
    if keys["Down"] and paddle_b.ycor() > -310:
        paddle_b.sety(paddle_b.ycor() - 8)

points = turtle.Turtle()
points.penup()
points.goto(0,230)
points.color("white")
points.write("0       0", align="center", font=("Arial", 24, "bold"))
turtle.hideturtle()

def update_score():
    points.clear() 
    points.write(f"{score_a}       {score_b}", align="center", font=("Arial", 24, "bold"))

while True:
    if score_a == 10 or score_b==10:
        winner = "Red Player" if score_a == 10 else "Blue Player"
        var = messagebox.askyesno("Nice game dude!!", f"{winner} wins!\nPlay again?")
        print(var)
        if (var):
            score_a =0
            score_b =0
            update_score()
            ball.goto(0,0)
            paddle_a.goto(-450,0)
            paddle_b.goto(450,0)
        else:
            break
    start_time = time.time()

    wn.update()
    move_paddles()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 320:
        ball.sety(320)
        ball.dy *= -1

    if ball.ycor() < -320:
        ball.sety(-320)
        ball.dy *= -1

    if ball.xcor() > 490:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        print(f"Red player: {score_a} | Blue player: {score_b}")
        update_score()
        


    if ball.xcor() < -490:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        print(f"Red player: {score_a} | Blue player: {score_b}")
        update_score()


    if (ball.xcor() >= 435 and ball.xcor() <=450) and (ball.ycor() <= paddle_b.ycor() + 60 and ball.ycor() >= paddle_b.ycor() - 60):
        if ball.dx > 0:
            ball.setx(434)
            ball.dx *= -1
    if (ball.xcor() <=-435 and ball.xcor() >=-450) and (ball.ycor() <= paddle_a.ycor() + 60 and ball.ycor() >= paddle_a.ycor() -60):
        if ball.dx < 0:
            ball.setx(-434)
            ball.dx *= -1

    frame_time = time.time() - start_time

    if frame_time < 1/60:
        time.sleep((1/60) -frame_time)