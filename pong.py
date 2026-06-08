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
easter67 = False
easter76 = False

pause = False
game_started = False 
ball_delay_frames = 0

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

def toggle_pause():
    global pause
    if not game_started: return 
    pause = not pause
    if pause:
        pause_text.write("PAUSED", align="center", font=("Arial", 28, "bold"))
    else:
        pause_text.clear()
    wn.listen()

wn.listen()
wn.onkeypress(press_w, "w")
wn.onkeyrelease(release_w, "w")

wn.onkeypress(press_s, "s")
wn.onkeyrelease(release_s, "s")

wn.onkeypress(press_Up, "Up")
wn.onkeyrelease(release_Up, "Up")

wn.onkeypress(press_Down, "Down")
wn.onkeyrelease(release_Down, "Down")

wn.onkeypress(toggle_pause, "space")

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
points.hideturtle()

pause_text = turtle.Turtle()
pause_text.penup()
pause_text.goto(0,-30)
pause_text.color("yellow")
pause_text.hideturtle()

menu_art = turtle.Turtle()
menu_art.speed(0)
menu_art.color("white")
menu_art.penup()
menu_art.hideturtle()

def draw_menu():
    menu_art.clear()
    menu_art.goto(0, 120)
    menu_art.color("cyan")
    menu_art.write("ROLO-PONG", align="center", font=("Arial", 50, "bold"))
    
    menu_art.goto(0, -40)
    menu_art.shape("square")
    menu_art.color("green")
    menu_art.shapesize(stretch_wid=5, stretch_len=9)
    menu_art.stamp()
    
    menu_art.goto(0, -52)
    menu_art.color("white")
    menu_art.write("START GAME :D", align="center", font=("Arial", 16, "bold"))

def detect_button_click(x, y):
    global game_started
    if not game_started:
        if -90 <= x <= 90 and -90 <= y <= 10:
            menu_art.clear() 
            points.write("0       0", align="center", font=("Arial", 24, "bold")) 
            game_started = True
            wn.listen() 

wn.onclick(detect_button_click) 

def update_score():
    points.clear() 
    points.write(f"{score_a}       {score_b}", align="center", font=("Arial", 24, "bold"))

draw_menu()

paddle_a.hideturtle()
paddle_b.hideturtle()
ball.hideturtle()

elements_shown = False

while True:
    if not game_started:
        wn.update()
        time.sleep(1/60)
        continue
    
    if game_started and not elements_shown:
        paddle_a.showturtle()
        paddle_b.showturtle()
        ball.showturtle()
        elements_shown = True

    if score_a == 10 or score_b==10:
        winner = "Red Player" if score_a == 10 else "Blue Player"
        var = messagebox.askyesno("Nice game dude!!", f"{winner} wins!\nPlay again?")
        print(var)
        if (var):
            easter67 = False
            easter76 = False
            score_a =0
            score_b =0
            update_score()
            ball.goto(0,0)
            paddle_a.goto(-450,0)
            paddle_b.goto(450,0)
            pause = False
            pause_text.clear()
            ball_delay_frames = 0
            wn.listen()
        else:
            break
    start_time = time.time()

    if pause:
        wn.update()
        time.sleep(1/60)
        continue

    if(score_a == 6 and score_b==7 and easter67 == False):
        if messagebox.askyesno ("really?", "was this intentional??"):
            messagebox.showinfo ("alr bet", "ok dude, i trust you")
        else:
            messagebox.showinfo ("what a strange coincidence, huh?", "6767676767676767676767676767676767676767676767")
        easter67 = True
        wn.listen()

    if(score_b == 6 and score_a==7 and easter76==False):
        if messagebox.askyesno ("lil question here", "do you like the philadelfia 76ers?"):
            messagebox.showinfo ("yayy", "you know ball bro")
        else:
            messagebox.showinfo ("are you joking now?", "go google them NOW BRO")
        easter76 = True
        wn.listen()

    wn.update()
    move_paddles()

    if ball_delay_frames > 0:
        ball_delay_frames -= 1
    else:
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
        ball_delay_frames = 90

    if ball.xcor() < -490:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        print(f"Red player: {score_a} | Blue player: {score_b}")
        update_score()
        ball_delay_frames = 90

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
