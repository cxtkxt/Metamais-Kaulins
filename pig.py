import tkinter as tk
from tkinter import messagebox
import random
import os

BACKGROUND_COLOR = "#facfcf"
BUTTON_COLOR = "#dbb4b4"
TEXT_COLOR = "#f96e80"
FONT_NAME = "LEMON MILK"

DICE_IMAGE_SIZE = 9
PIG_IMAGE_SIZE = 2

player = 1
player1_score = 0
player2_score = 0

def load_image(file_name, scale):
    path = os.path.join(os.path.dirname(__file__), file_name)
    if os.path.exists(path):
        img = tk.PhotoImage(file=path)
        return img.subsample(scale, scale)
    return None

def roll_dice():
    global player, player1_score, player2_score

    roll = random.randint(1, 6)
    dice_number.config(text=str(roll))

    if roll == 1:
        if player == 1:
            player1_score = 0
        else:
            player2_score = 0

        update_scores()
        messagebox.showinfo("Pig", "Tu uzmeti 1! Visi punkti pazūd.")
    else:
        if player == 1:
            player1_score += roll
        else:
            player2_score += roll

        update_scores()

    if player1_score >= 100:
        messagebox.showinfo("Uzvara", "1. spēlētājs uzvarēja!")
        roll_button.config(state="disabled")
    elif player2_score >= 100:
        messagebox.showinfo("Uzvara", "2. spēlētājs uzvarēja!")
        roll_button.config(state="disabled")
    else:
        change_player()

def change_player():
    global player
    player = 2 if player == 1 else 1
    player_label.config(text=f"Gājiens: {player}. spēlētājs")

def update_scores():
    player1_label.config(text=f"1. spēlētājs: {player1_score}")
    player2_label.config(text=f"2. spēlētājs: {player2_score}")

def reset_game():
    global player, player1_score, player2_score

    player = 1
    player1_score = 0
    player2_score = 0

    dice_number.config(text="0")
    player_label.config(text="Gājiens: 1. spēlētājs")
    update_scores()
    roll_button.config(state="normal")

window = tk.Tk()
window.title("Pig")
window.geometry("800x500")
window.configure(bg=BACKGROUND_COLOR)

main_frame = tk.Frame(window, bg=BACKGROUND_COLOR)
main_frame.pack(expand=True)

left_frame = tk.Frame(main_frame, bg=BACKGROUND_COLOR)
left_frame.grid(row=0, column=0, padx=30)

center_frame = tk.Frame(main_frame, bg=BACKGROUND_COLOR)
center_frame.grid(row=0, column=1, padx=30)

right_frame = tk.Frame(main_frame, bg=BACKGROUND_COLOR)
right_frame.grid(row=0, column=2, padx=30)

# 🔥 CENTER FIX
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=3)
main_frame.grid_columnconfigure(2, weight=1)
main_frame.grid_rowconfigure(0, weight=1)

dice_image = load_image("dice.png", DICE_IMAGE_SIZE)
pig_image = load_image("pig.png", PIG_IMAGE_SIZE)

if dice_image:
    dice_image_label = tk.Label(left_frame, image=dice_image, bg=BACKGROUND_COLOR)
    dice_image_label.pack()

title = tk.Label(center_frame, text="PIG", font=(FONT_NAME, 28), bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
title.pack(pady=10)

player_label = tk.Label(center_frame, text="Gājiens: 1. spēlētājs", font=(FONT_NAME, 12), bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
player_label.pack(pady=5)

dice_number = tk.Label(center_frame, text="0", font=(FONT_NAME, 40), bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
dice_number.pack(pady=10)

player1_label = tk.Label(center_frame, text="1. spēlētājs: 0", font=(FONT_NAME, 11), bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
player1_label.pack()

player2_label = tk.Label(center_frame, text="2. spēlētājs: 0", font=(FONT_NAME, 11), bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
player2_label.pack()

roll_button = tk.Button(center_frame, text="Mest", command=roll_dice, width=15, font=(FONT_NAME, 10), bg=BUTTON_COLOR, fg=TEXT_COLOR)
roll_button.pack(pady=10)

reset_button = tk.Button(center_frame, text="Reset", command=reset_game, width=15, font=(FONT_NAME, 10), bg=BUTTON_COLOR, fg=TEXT_COLOR)
reset_button.pack()

if pig_image:
    pig_image_label = tk.Label(right_frame, image=pig_image, bg=BACKGROUND_COLOR)
    pig_image_label.pack()

window.mainloop()