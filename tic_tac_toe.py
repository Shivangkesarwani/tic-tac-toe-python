from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe")
root.geometry("400x500")
root.resizable(False, False)

player1 = StringVar()
player2 = StringVar()

current_player = "X"
x_score = 0
o_score = 0
buttons = []

# ---------- Functions ----------

def start_game():
    if player1.get() == "" or player2.get() == "":
        messagebox.showwarning("Warning", "Enter both player names!")
        return

    start_frame.pack_forget()
    game_frame.pack()

def update_score():
    score_label.config(
        text=f"{player1.get()} (X): {x_score}    {player2.get()} (O): {o_score}"
    )

def check_winner():
    global x_score, o_score

    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for combo in wins:
        a, b, c = combo

        if buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] != "":
            for i in combo:
                buttons[i].config(bg="lightgreen")

            winner = buttons[a]["text"]

            if winner == "X":
                x_score += 1
                winner_name = player1.get()
            else:
                o_score += 1
                winner_name = player2.get()

            update_score()

            root.after(
                500,
                lambda: (
                    messagebox.showinfo("Winner", f"{winner_name} Wins!"),
                    reset_board()
                )
            )
            return

    if all(btn["text"] != "" for btn in buttons):
        messagebox.showinfo("Draw", "Match Draw!")
        reset_board()

def button_click(index):
    global current_player

    if buttons[index]["text"] == "":
        buttons[index]["text"] = current_player

        check_winner()

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

        turn_label.config(text=f"Turn: {current_player}")

def reset_board():
    global current_player

    current_player = "X"
    turn_label.config(text="Turn: X")

    for btn in buttons:
        btn.config(text="", bg="SystemButtonFace")

def restart_game():
    global x_score, o_score

    x_score = 0
    o_score = 0

    update_score()
    reset_board()

# ---------- Start Frame ----------

start_frame = Frame(root)

Label(
    start_frame,
    text="Tic Tac Toe",
    font=("Arial", 20, "bold")
).pack(pady=20)

Label(start_frame, text="Player 1 (X)").pack()
Entry(start_frame, textvariable=player1).pack(pady=5)

Label(start_frame, text="Player 2 (O)").pack()
Entry(start_frame, textvariable=player2).pack(pady=5)

Button(
    start_frame,
    text="Start Game",
    command=start_game
).pack(pady=20)

start_frame.pack()

# ---------- Game Frame ----------

game_frame = Frame(root)

score_label = Label(
    game_frame,
    text="Score",
    font=("Arial", 12, "bold")
)
score_label.pack(pady=10)

turn_label = Label(
    game_frame,
    text="Turn: X",
    font=("Arial", 14)
)
turn_label.pack()

board = Frame(game_frame)
board.pack(pady=10)

for i in range(9):
    btn = Button(
        board,
        text="",
        width=6,
        height=3,
        font=("Arial", 20),
        command=lambda i=i: button_click(i)
    )

    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

Button(
    game_frame,
    text="Restart Game",
    font=("Arial", 12),
    command=restart_game
).pack(pady=10)

root.mainloop()