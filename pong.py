import tkinter as tk
import random

# ---------------- WINDOW ---------------- #

WIDTH = 900
HEIGHT = 550

BALL_SIZE = 20

PADDLE_WIDTH = 18
PADDLE_HEIGHT = 110

PADDLE_SPEED = 25

WIN_SCORE = 5

root = tk.Tk()
root.title("Modern Pong Game")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.configure(bg="#0f172a")
root.resizable(False, False)

canvas = tk.Canvas(
    root,
    width=WIDTH,
    height=HEIGHT,
    bg="#0f172a",
    highlightthickness=0
)
canvas.pack()

# ---------------- CENTER LINE ---------------- #

for i in range(0, HEIGHT, 35):
    canvas.create_line(
        WIDTH//2,
        i,
        WIDTH//2,
        i+18,
        fill="#334155",
        width=4
    )

# ---------------- TITLE ---------------- #

canvas.create_text(
    WIDTH//2,
    25,
    text="PONG GAME",
    fill="#38bdf8",
    font=("Helvetica", 20, "bold")
)

# ---------------- SCORE ---------------- #

left_score = 0
right_score = 0

score_text = canvas.create_text(
    WIDTH//2,
    60,
    text="0   :   0",
    fill="white",
    font=("Helvetica", 34, "bold")
)

# ---------------- CONTROLS ---------------- #

canvas.create_text(
    WIDTH//2,
    HEIGHT-18,
    text="Left Player : W / S        Right Player : ↑ / ↓",
    fill="#94a3b8",
    font=("Arial",12)
)

# ---------------- PADDLES ---------------- #

left_paddle = canvas.create_rectangle(
    40,
    HEIGHT//2-PADDLE_HEIGHT//2,
    40+PADDLE_WIDTH,
    HEIGHT//2+PADDLE_HEIGHT//2,
    fill="#22c55e",
    outline=""
)

right_paddle = canvas.create_rectangle(
    WIDTH-58,
    HEIGHT//2-PADDLE_HEIGHT//2,
    WIDTH-40,
    HEIGHT//2+PADDLE_HEIGHT//2,
    fill="#22c55e",
    outline=""
)

# ---------------- BALL SHADOW ---------------- #

shadow = canvas.create_oval(
    WIDTH//2-BALL_SIZE//2+3,
    HEIGHT//2-BALL_SIZE//2+3,
    WIDTH//2+BALL_SIZE//2+3,
    HEIGHT//2+BALL_SIZE//2+3,
    fill="#334155",
    outline=""
)

# ---------------- BALL ---------------- #

ball = canvas.create_oval(
    WIDTH//2-BALL_SIZE//2,
    HEIGHT//2-BALL_SIZE//2,
    WIDTH//2+BALL_SIZE//2,
    HEIGHT//2+BALL_SIZE//2,
    fill="#38bdf8",
    outline=""
)

ball_dx = random.choice([-6, 6])
ball_dy = random.choice([-5, 5])

game_over = False

# ---------------- PADDLE MOVEMENT ---------------- #

def move_left_up(event):
    canvas.move(left_paddle, 0, -PADDLE_SPEED)

def move_left_down(event):
    canvas.move(left_paddle, 0, PADDLE_SPEED)

def move_right_up(event):
    canvas.move(right_paddle, 0, -PADDLE_SPEED)

def move_right_down(event):
    canvas.move(right_paddle, 0, PADDLE_SPEED)

root.bind("w", move_left_up)
root.bind("s", move_left_down)
root.bind("<Up>", move_right_up)
root.bind("<Down>", move_right_down)
# ---------------- FUNCTIONS ---------------- #

def keep_paddles_inside():
    for paddle in [left_paddle, right_paddle]:
        x1, y1, x2, y2 = canvas.coords(paddle)

        if y1 < 0:
            canvas.move(paddle, 0, -y1)

        if y2 > HEIGHT:
            canvas.move(paddle, 0, HEIGHT - y2)


def reset_ball():
    global ball_dx, ball_dy

    canvas.coords(
        ball,
        WIDTH//2-BALL_SIZE//2,
        HEIGHT//2-BALL_SIZE//2,
        WIDTH//2+BALL_SIZE//2,
        HEIGHT//2+BALL_SIZE//2
    )

    canvas.coords(
        shadow,
        WIDTH//2-BALL_SIZE//2+3,
        HEIGHT//2-BALL_SIZE//2+3,
        WIDTH//2+BALL_SIZE//2+3,
        HEIGHT//2+BALL_SIZE//2+3
    )

    ball_dx = random.choice([-6, 6])
    ball_dy = random.choice([-5, 5])


def update_score():
    canvas.itemconfig(
        score_text,
        text=f"{left_score}   :   {right_score}"
    )


def show_winner(text):
    global game_over

    game_over = True

    canvas.create_rectangle(
        180,
        170,
        720,
        380,
        fill="#1e293b",
        outline="#38bdf8",
        width=3
    )

    canvas.create_text(
        WIDTH//2,
        230,
        text=text,
        fill="#22c55e",
        font=("Helvetica", 34, "bold")
    )

    canvas.create_text(
        WIDTH//2,
        290,
        text=f"Final Score : {left_score} : {right_score}",
        fill="white",
        font=("Helvetica", 20)
    )

    canvas.create_text(
        WIDTH//2,
        340,
        text="Close the window to exit",
        fill="#94a3b8",
        font=("Arial", 14)
    )


def check_winner():
    if left_score >= WIN_SCORE:
        show_winner("PLAYER 1 WINS!")

    elif right_score >= WIN_SCORE:
        show_winner("PLAYER 2 WINS!")

   # ---------------- GAME LOOP ---------------- #

def game_loop():
    global ball_dx, ball_dy
    global left_score, right_score

    if game_over:
        return

    canvas.move(ball, ball_dx, ball_dy)
    canvas.move(shadow, ball_dx, ball_dy)

    bx1, by1, bx2, by2 = canvas.coords(ball)

    # Top & Bottom Collision
    if by1 <= 0 or by2 >= HEIGHT:
        ball_dy *= -1

    # Left Paddle Collision
    lx1, ly1, lx2, ly2 = canvas.coords(left_paddle)

    if (
        bx1 <= lx2 and
        bx2 >= lx1 and
        by2 >= ly1 and
        by1 <= ly2
    ):
        ball_dx = abs(ball_dx)

    # Right Paddle Collision
    rx1, ry1, rx2, ry2 = canvas.coords(right_paddle)

    if (
        bx2 >= rx1 and
        bx1 <= rx2 and
        by2 >= ry1 and
        by1 <= ry2
    ):
        ball_dx = -abs(ball_dx)

    # Right Player Scores
    if bx1 <= 0:
        right_score += 1
        update_score()
        check_winner()

        if not game_over:
            reset_ball()

    # Left Player Scores
    if bx2 >= WIDTH:
        left_score += 1
        update_score()
        check_winner()

        if not game_over:
            reset_ball()

    keep_paddles_inside()

    root.after(20, game_loop)


# ---------------- START GAME ---------------- #

game_loop()

root.mainloop()     