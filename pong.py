import turtle
import tkinter
from tkinter import messagebox
import time
import random

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
paddle_a.goto(10000, 10000)

paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(10000, 10000)


ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(10000, 10000)
ball.dx = random.choice([6, -6])
ball.dy = random.choice([6, -6])

score_a = 0
score_b = 0
easter67 = False
easter76 = False

pause = False
game_started = False 
ball_delay_frames = 0
game_mode = "classic"
cpu_difficulty = "medium"
sub_menu = False

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
        draw_quit_button()
    else:
        pause_text.clear()
        quit_art.clear()
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
        
    if game_mode == "cpu":
        if cpu_difficulty == "easy":
            speed = 3.8
            # El modo fácil conserva la restricción de mirar la pelota solo cuando se acerca
            if ball.dx > 0:
                if paddle_b.ycor() < ball.ycor() and paddle_b.ycor() < 310:
                    paddle_b.sety(paddle_b.ycor() + speed)
                elif paddle_b.ycor() > ball.ycor() and paddle_b.ycor() > -310:
                    paddle_b.sety(paddle_b.ycor() - speed)
        else:
            # Medium y Hard ahora rastrean de forma continua en cualquier dirección
            speed = 4.9 if cpu_difficulty == "medium" else 5.6
            if paddle_b.ycor() < ball.ycor() and paddle_b.ycor() < 310:
                paddle_b.sety(paddle_b.ycor() + speed)
            elif paddle_b.ycor() > ball.ycor() and paddle_b.ycor() > -310:
                paddle_b.sety(paddle_b.ycor() - speed)
    else:
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
pause_text.goto(0, 40)
pause_text.color("yellow")
pause_text.hideturtle()

menu_art = turtle.Turtle()
menu_art.speed(0)
menu_art.penup()
menu_art.hideturtle()

quit_art = turtle.Turtle()
quit_art.speed(0)
quit_art.color("white")
quit_art.penup()
quit_art.hideturtle()

def draw_menu_button(x, y, color, text):
    menu_art.goto(x, y)
    menu_art.shape("square")
    menu_art.color(color)
    menu_art.shapesize(stretch_wid=5, stretch_len=9)
    menu_art.stamp()
    
    menu_art.goto(x, y - 12)
    menu_art.color("white")
    menu_art.write(text, align="center", font=("Arial", 16, "bold"))

def draw_menu():
    menu_art.clear()
    menu_art.goto(0, 150)
    menu_art.color("cyan")
    menu_art.write("ROLO-PONG", align="center", font=("Arial", 50, "bold"))
    
    draw_menu_button(-220, -40, "purple", "INFINITE")
    draw_menu_button(0, -40, "green", "CLASSIC")
    draw_menu_button(220, -40, "orange", "VS CPU")

def draw_cpu_menu():
    menu_art.clear()
    menu_art.goto(0, 150)
    menu_art.color("cyan")
    menu_art.write("SELECT DIFFICULTY", align="center", font=("Arial", 40, "bold"))
    
    draw_menu_button(-240, -40, "gold", "EASY CPU")
    draw_menu_button(0, -40, "darkorange", "MEDIUM CPU")
    draw_menu_button(240, -40, "crimson", "HARD CPU")

def draw_quit_button():
    quit_art.clear()
    quit_art.goto(0, -60)
    quit_art.shape("square")
    quit_art.color("red")
    quit_art.shapesize(stretch_wid=2.5, stretch_len=6)
    quit_art.stamp()
    quit_art.goto(0, -75)
    quit_art.color("white")
    quit_art.write("QUIT", align="center", font=("Arial", 14, "bold"))

def return_to_menu():
    global game_started, pause, score_a, score_b, easter67, easter76, sub_menu
    pause = False
    game_started = False
    sub_menu = False
    score_a = 0
    score_b = 0
    pause_text.clear()
    quit_art.clear()
    points.clear()
    paddle_a.goto(10000, 10000)
    paddle_b.goto(10000, 10000)
    ball.goto(10000, 10000)
    draw_menu()

def detect_click(x, y):
    global game_started, game_mode, cpu_difficulty, sub_menu
    if not game_started:
        if not sub_menu:
            if -90 <= x <= 90 and -90 <= y <= 10:
                game_mode = "classic"
                start_match()
            elif -310 <= x <= -130 and -90 <= y <= 10:
                game_mode = "infinite"
                start_match()
            elif 130 <= x <= 310 and -90 <= y <= 10:
                game_mode = "cpu"
                sub_menu = True
                draw_cpu_menu()
        else:
            if -330 <= x <= -150 and -90 <= y <= 10:
                cpu_difficulty = "easy"
                start_match()
            elif -90 <= x <= 90 and -90 <= y <= 10:
                cpu_difficulty = "medium"
                start_match()
            elif 150 <= x <= 330 and -90 <= y <= 10:
                cpu_difficulty = "hard"
                start_match()
    elif pause:
        if -60 <= x <= 60 and -85 <= y <= -35:
            return_to_menu()

def start_match():
    global game_started, sub_menu
    sub_menu = False
    menu_art.clear()
    points.write("0       0", align="center", font=("Arial", 24, "bold"))
    paddle_a.goto(-450, 0)
    paddle_b.goto(450, 0)
    ball.goto(0, 0)
    game_started = True
    wn.listen()

wn.onclick(detect_click)

def update_score():
    points.clear() 
    points.write(f"{score_a}       {score_b}", align="center", font=("Arial", 24, "bold"))

draw_menu()

while True:
    if not game_started:
        wn.update()
        time.sleep(1/60)
        continue

    if game_mode != "infinite" and (score_a == 10 or score_b == 10):
        winner = "Red Player" if score_a == 10 else "Blue Player"
        var = messagebox.askyesno("Nice game dude!!", f"{winner} wins!\nPlay again?")
        if (var):
            easter67 = False
            easter76 = False
            score_a = 0
            score_b = 0
            update_score()
            ball.goto(0,0)
            paddle_a.goto(-450,0)
            paddle_b.goto(450,0)
            pause = False
            pause_text.clear()
            ball_delay_frames = 0
            wn.listen()
        else:
            return_to_menu()
            continue
            
    start_time = time.time()

    if pause:
        wn.update()
        time.sleep(1/60)
        continue

    if game_mode != "infinite":
        if(score_a == 6 and score_b==7 and easter67 == False):
            if messagebox.askyesno ("really?", "was this intentional??"):
                messagebox.showinfo ("what a strange score, huh?", "6767676767676767676767676767676767676767676767")
            else:
                messagebox.showinfo ("alr bet", "ok dude, i trust you")
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
        ball.dx = random.choice([6, -6])
        ball.dy = random.choice([6, -6])
        score_a += 1
        print(f"Red player: {score_a} | Blue player: {score_b}")
        update_score()
        ball_delay_frames = 90

    if ball.xcor() < -490:
        ball.goto(0, 0)
        ball.dx = random.choice([6, -6])
        ball.dy = random.choice([6, -6])
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
