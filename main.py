import turtle
import random
screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch The Turtle")

score_turtle = turtle.Turtle()
game_over = False
countdown_turtle = turtle.Turtle()

def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.color("dark blue")
    countdown_turtle.penup()

    top_hight = screen.window_height() / 2
    y = top_hight * 0.8
    countdown_turtle.setpos(0,y)
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write("Kalan Zaman: {}".format(time),align="center",font=("arial",15,"normal"))
        screen.ontimer(lambda :countdown(time-1), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtle()
        countdown_turtle.write("Kalan Zaman: Game Over", align="center", font=("arial", 15, "normal"))
def score():
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()
    top_hight = screen.window_height() / 2
    y = top_hight * 0.9
    score_turtle.setpos(0,y)
    score_turtle.write("Score: 0",align="center",font=("arial",15,"normal"))
grid_size = 10
scor=0
turtle_list = []
def main_turtle(x,y):
    t = turtle.Turtle()
    def up_score(x,y):
        global scor
        scor += 1
        score_turtle.clear()
        score_turtle.write("Score: {}".format(scor), align="center", font=("arial", 15, "normal"))
    t.onclick(up_score)
    t.shape("turtle")
    t.color("dark green")
    t.penup()
    t.shapesize(2,2)
    t.goto(x*grid_size,y*grid_size)
    turtle_list.append(t)
x_coordinates = [-20,-10,0,10,20]
y_coordinates = [20,10,0,-10]
def for_turtle():
    for x in x_coordinates:
        for y in y_coordinates:
            main_turtle(x,y)
def hide_turtle():
    for t in turtle_list:
        t.hideturtle()
def show_turtle_random():
    if not game_over:
        hide_turtle()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtle_random,500)
def start_game():
    turtle.tracer(0)
    countdown(10)
    for_turtle()
    score()
    hide_turtle()
    show_turtle_random()
    turtle.tracer(1)
start_game()
turtle.mainloop()