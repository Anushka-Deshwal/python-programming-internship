import turtle
import time
import random

# Screen Setup
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Snake Body
segments = []

# Score
score = 0
high_score = 0

# Score Display
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(
    "Score: 0  High Score: 0",
    align="center",
    font=("Arial", 16, "bold")
)

# Movement Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)

    if head.direction == "down":
        head.sety(head.ycor() - 20)

    if head.direction == "left":
        head.setx(head.xcor() - 20)

    if head.direction == "right":
        head.setx(head.xcor() + 20)

# Controls
screen.listen()
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_left, "a")
screen.onkeypress(go_right, "d")

# Game Over Text
game_over_pen = turtle.Turtle()
game_over_pen.hideturtle()
game_over_pen.color("red")
game_over_pen.penup()

delay = 0.1

# Main Game Loop
while True:
    screen.update()

    # Border Collision
    if (
        head.xcor() > 290 or
        head.xcor() < -290 or
        head.ycor() > 290 or
        head.ycor() < -290
    ):

        game_over_pen.goto(0, 0)
        game_over_pen.write(
            "GAME OVER",
            align="center",
            font=("Arial", 28, "bold")
        )

        screen.update()
        time.sleep(2)
        game_over_pen.clear()

        head.goto(0, 0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()
        score = 0

    # Food Collision
    if head.distance(food) < 20:

        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("lightgreen")
        new_segment.penup()

        segments.append(new_segment)

        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(
            f"Score: {score}  High Score: {high_score}",
            align="center",
            font=("Arial", 16, "bold")
        )

    # Move Body
    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Self Collision
    for segment in segments:
        if segment.distance(head) < 20:

            game_over_pen.goto(0, 0)
            game_over_pen.write(
                "GAME OVER",
                align="center",
                font=("Arial", 28, "bold")
            )

            screen.update()
            time.sleep(2)
            game_over_pen.clear()

            head.goto(0, 0)
            head.direction = "stop"

            for seg in segments:
                seg.goto(1000, 1000)

            segments.clear()
            score = 0

    time.sleep(delay)

screen.mainloop()