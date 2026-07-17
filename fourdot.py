import tkinter as tk
from tkinter import messagebox

ROWS = 6
COLS = 7
CELL = 80

board = [["" for _ in range(COLS)] for _ in range(ROWS)]
current_player = "R"

root = tk.Tk()
root.title("Connect Four")
root.configure(bg="#1E1E2F")
root.resizable(False, False)

canvas = tk.Canvas(
    root,
    width=COLS * CELL,
    height=ROWS * CELL,
    bg="#1565C0",
    highlightthickness=0
)
canvas.pack(pady=10)


def draw_board():
    canvas.delete("all")

    for r in range(ROWS):
        for c in range(COLS):
            x1 = c * CELL + 5
            y1 = r * CELL + 5
            x2 = x1 + CELL - 10
            y2 = y1 + CELL - 10

            color = "white"

            if board[r][c] == "R":
                color = "red"
            elif board[r][c] == "Y":
                color = "yellow"

            canvas.create_oval(
                x1,
                y1,
                x2,
                y2,
                fill=color,
                outline="black",
                width=2
            )


def show_winner(player):
    win = tk.Toplevel(root)
    win.title("🏆 Game Over")
    win.geometry("400x300")
    win.configure(bg="#1E1E2F")
    win.resizable(False, False)
    win.grab_set()

    winner = "🔴 Red" if player == "R" else "🟡 Yellow"

    tk.Label(
        win,
        text="🏆",
        font=("Arial", 55),
        bg="#1E1E2F"
    ).pack(pady=(15, 5))

    tk.Label(
        win,
        text="Congratulations!",
        font=("Arial", 22, "bold"),
        fg="white",
        bg="#1E1E2F"
    ).pack()

    tk.Label(
        win,
        text=f"{winner} Player Wins!",
        font=("Arial", 18, "bold"),
        fg="#FFD700",
        bg="#1E1E2F"
    ).pack(pady=10)

    frame = tk.Frame(win, bg="#1E1E2F")
    frame.pack(pady=20)

    tk.Button(
        frame,
        text="🔄 Play Again",
        font=("Arial", 12, "bold"),
        bg="#4CAF50",
        fg="white",
        width=12,
        command=lambda: [win.destroy(), reset_game()]
    ).grid(row=0, column=0, padx=10)

    tk.Button(
        frame,
        text="❌ Exit",
        font=("Arial", 12, "bold"),
        bg="#E53935",
        fg="white",
        width=12,
        command=root.destroy
    ).grid(row=0, column=1, padx=10)


def drop_piece(col):
    global current_player

    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == "":
            board[row][col] = current_player

            draw_board()

            if check_win(current_player):
                show_winner(current_player)
                return

            if board_full():
                messagebox.showinfo("Draw", "🤝 Game Draw!")
                reset_game()
                return

            current_player = "Y" if current_player == "R" else "R"

            status.config(
                text=f"Turn: {'🔴 Red' if current_player=='R' else '🟡 Yellow'}"
            )
            return


def board_full():
    return all(board[0][c] != "" for c in range(COLS))


def check_win(piece):

    # Horizontal
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c + i] == piece for i in range(4)):
                return True

    # Vertical
    for r in range(ROWS - 3):
        for c in range(COLS):
            if all(board[r + i][c] == piece for i in range(4)):
                return True

    # Diagonal \
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r + i][c + i] == piece for i in range(4)):
                return True

    # Diagonal /
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(board[r - i][c + i] == piece for i in range(4)):
                return True

    return False
def reset_game():
    global board, current_player

    board = [["" for _ in range(COLS)] for _ in range(ROWS)]
    current_player = "R"

    draw_board()

    status.config(text="Turn: 🔴 Red")


button_frame = tk.Frame(root, bg="#1E1E2F")
button_frame.pack()

for c in range(COLS):
    tk.Button(
        button_frame,
        text="▼",
        font=("Arial", 16, "bold"),
        width=4,
        command=lambda col=c: drop_piece(col),
        bg="#3949AB",
        fg="white",
        activebackground="#5C6BC0",
        activeforeground="white",
        cursor="hand2"
    ).grid(row=0, column=c, padx=2, pady=2)


status = tk.Label(
    root,
    text="Turn: 🔴 Red",
    font=("Arial", 16, "bold"),
    bg="#1E1E2F",
    fg="white"
)
status.pack(pady=10)


tk.Button(
    root,
    text="Restart Game",
    command=reset_game,
    font=("Arial", 14, "bold"),
    bg="#43A047",
    fg="white",
    activebackground="#2E7D32",
    activeforeground="white",
    cursor="hand2",
    width=15
).pack(pady=10)


draw_board()

root.mainloop()