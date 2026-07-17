import tkinter as tk
from tkinter import messagebox

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("450x600")
root.resizable(False, False)
root.configure(bg="#0f172a")

# ---------------- VARIABLES ----------------
current_player = "X"
board = [""] * 9

x_score = 0
o_score = 0
tie_score = 0

winning_cells = []

# ---------------- FUNCTIONS ----------------

def update_score():
    score_label.config(
        text=f"X: {x_score}    O: {o_score}    Tie: {tie_score}"
    )


def check_winner():
    winning_combinations = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for combo in winning_combinations:
        a, b, c = combo

        if board[a] == board[b] == board[c] != "":
            return board[a], combo

    return None, None


def highlight_winner(combo):
    for index in combo:
        buttons[index].config(bg="#22c55e")


def button_click(index):
    global current_player
    global x_score, o_score, tie_score

    if board[index] != "":
        return

    board[index] = current_player

    if current_player == "X":
        buttons[index].config(
            text="X",
            fg="#3b82f6"
        )
    else:
        buttons[index].config(
            text="O",
            fg="#ef4444"
        )

    winner, combo = check_winner()

    if winner:
        highlight_winner(combo)

        if winner == "X":
            x_score += 1
        else:
            o_score += 1

        update_score()

        root.after(
            500,
            lambda: [
                messagebox.showinfo(
                    "Winner",
                    f"🎉 Player {winner} Wins!"
                ),
                new_game()
            ]
        )
        return

    if "" not in board:
        tie_score += 1
        update_score()

        root.after(
            300,
            lambda: [
                messagebox.showinfo(
                    "Tie",
                    "🤝 It's a Tie!"
                ),
                new_game()
            ]
        )
        return

    current_player = "O" if current_player == "X" else "X"

    if current_player == "X":
        turn_label.config(
            text="Player Turn: X",
            fg="#3b82f6"
        )
    else:
        turn_label.config(
            text="Player Turn: O",
            fg="#ef4444"
        )


def new_game():
    global board, current_player

    board = [""] * 9
    current_player = "X"

    turn_label.config(
        text="Player Turn: X",
        fg="#3b82f6"
    )

    for btn in buttons:
        btn.config(
            text="",
            bg="#1e293b"
        )


def reset_scores():
    global x_score, o_score, tie_score

    x_score = 0
    o_score = 0
    tie_score = 0

    update_score()
    new_game()


# ---------------- TITLE ----------------

title = tk.Label(
    root,
    text="TIC TAC TOE",
    font=("Arial", 24, "bold"),
    bg="#0f172a",
    fg="#38bdf8"
)
title.pack(pady=15)

# ---------------- TURN LABEL ----------------

turn_label = tk.Label(
    root,
    text="Player Turn: X",
    font=("Arial", 16, "bold"),
    bg="#0f172a",
    fg="#3b82f6"
)
turn_label.pack()

# ---------------- SCORE LABEL ----------------

score_label = tk.Label(
    root,
    text="X: 0    O: 0    Tie: 0",
    font=("Arial", 14, "bold"),
    bg="#0f172a",
    fg="#22c55e"
)
score_label.pack(pady=15)

# ---------------- GAME BOARD ----------------

frame = tk.Frame(root, bg="#0f172a")
frame.pack()

buttons = []

for row in range(3):
    for col in range(3):
        index = row * 3 + col

        btn = tk.Button(
            frame,
            text="",
            font=("Arial", 28, "bold"),
            width=4,
            height=2,
            bg="#1e293b",
            fg="white",
            activebackground="#334155",
            relief="flat",
            bd=0,
            command=lambda i=index: button_click(i)
        )

        btn.grid(
            row=row,
            column=col,
            padx=6,
            pady=6
        )

        buttons.append(btn)

# ---------------- CONTROL BUTTONS ----------------

new_btn = tk.Button(
    root,
    text="🔄 New Game",
    font=("Arial", 12, "bold"),
    bg="#22c55e",
    fg="white",
    width=18,
    relief="flat",
    command=new_game
)
new_btn.pack(pady=15)

reset_btn = tk.Button(
    root,
    text="🗑️ Reset Scores",
    font=("Arial", 12, "bold"),
    bg="#f97316",
    fg="white",
    width=18,
    relief="flat",
    command=reset_scores
)
reset_btn.pack()

# ---------------- FOOTER ----------------

footer = tk.Label(
    root,
    text="Built with Python & Tkinter",
    font=("Arial", 10),
    bg="#0f172a",
    fg="gray"
)
footer.pack(side="bottom", pady=10)

# ---------------- START ----------------

root.mainloop()