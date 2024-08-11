import tkinter as tk
from tkinter import messagebox
import random

def check_winner():
    global winner
    for combo in [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8],[2,4,6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            winner = True
            root.quit()
    # Check for draw
    if all(button["text"] != "" for button in buttons) and not winner:
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        root.quit()

def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        if not winner:
            toggle_player()
            ai_move()

def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")

def ai_move():
    global winner
    # Try to win
    for combo in [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8],[2,4,6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == "O" and buttons[combo[2]]["text"] == "":
            buttons[combo[2]].config(text="O")
            check_winner()
            if not winner:
                toggle_player()
            return
        if buttons[combo[1]]["text"] == buttons[combo[2]]["text"] == "O" and buttons[combo[0]]["text"] == "":
            buttons[combo[0]].config(text="O")
            check_winner()
            if not winner:
                toggle_player()
            return
        if buttons[combo[0]]["text"] == buttons[combo[2]]["text"] == "O" and buttons[combo[1]]["text"] == "":
            buttons[combo[1]].config(text="O")
            check_winner()
            if not winner:
                toggle_player()
            return

    # Try to block
    for combo in [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8],[2,4,6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == "X" and buttons[combo[2]]["text"] == "":
            buttons[combo[2]].config(text="O")
            check_winner()
            if not winner:
                toggle_player()
            return
        if buttons[combo[1]]["text"] == buttons[combo[2]]["text"] == "X" and buttons[combo[0]]["text"] == "":
            buttons[combo[0]].config(text="O")
            check_winner()
            if not winner:
                toggle_player()
            return
        if buttons[combo[0]]["text"] == buttons[combo[2]]["text"] == "X" and buttons[combo[1]]["text"] == "":
            buttons[combo[1]].config(text="O")
            check_winner()
            if not winner:
                toggle_player()
            return

    # Choose a random empty spot
    empty_buttons = [i for i in range(9) if buttons[i]["text"] == ""]
    if empty_buttons:
        random_index = random.choice(empty_buttons)
        buttons[random_index].config(text="O")
        check_winner()
        if not winner:
            toggle_player()

root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = [tk.Button(root, text="", font=("normal", 25), width=6, height=2, command=lambda i=i: button_click(i)) for i in range(9)]

for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

current_player = "X"
winner = False
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()

