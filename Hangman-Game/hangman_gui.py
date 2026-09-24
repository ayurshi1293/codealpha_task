import tkinter as tk
from tkinter import messagebox
import random

# Words for the game
WORDS = ["PYTHON", "COMPUTER", "PROGRAM", "KEYBOARD", "SOFTWARE"]

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Hangman Game")
        self.root.geometry("600x650")
        self.root.resizable(False, False)

        self.word = ""
        self.guessed = set()
        self.wrong_guesses = 0
        self.max_wrong = 6

        self.create_ui()
        self.new_game()

    def create_ui(self):
        # Title
        title = tk.Label(
            self.root,
            text="🎮 HANGMAN GAME",
            font=("Arial", 26, "bold")
        )
        title.pack(pady=20)

        # Instructions
        tk.Label(
            self.root,
            text="Guess the hidden word one letter at a time!",
            font=("Arial", 12)
        ).pack()

        # Word display
        self.word_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 30, "bold")
        )
        self.word_label.pack(pady=30)

        # Attempts
        self.attempts_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 14)
        )
        self.attempts_label.pack()

        # Guessed letters
        self.guessed_label = tk.Label(
            self.root,
            text="Guessed letters: None",
            font=("Arial", 12)
        )
        self.guessed_label.pack(pady=10)

        # Letter buttons
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(pady=20)

        self.buttons = {}

        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for index, letter in enumerate(letters):
            button = tk.Button(
                self.buttons_frame,
                text=letter,
                width=4,
                height=2,
                font=("Arial", 11, "bold"),
                command=lambda l=letter: self.guess_letter(l)
            )

            button.grid(
                row=index // 6,
                column=index % 6,
                padx=4,
                pady=4
            )

            self.buttons[letter] = button

        # New Game button
        self.new_game_button = tk.Button(
            self.root,
            text="🔄 NEW GAME",
            font=("Arial", 13, "bold"),
            command=self.new_game
        )
        self.new_game_button.pack(pady=15)

    def new_game(self):
        self.word = random.choice(WORDS)
        self.guessed = set()
        self.wrong_guesses = 0

        for button in self.buttons.values():
            button.config(state=tk.NORMAL)

        self.update_display()

    def guess_letter(self, letter):
        if letter in self.guessed:
            return

        self.guessed.add(letter)

        # Disable clicked button
        self.buttons[letter].config(state=tk.DISABLED)

        if letter not in self.word:
            self.wrong_guesses += 1

        self.update_display()

        # Check win
        if all(letter in self.guessed for letter in self.word):
            messagebox.showinfo(
                "🎉 You Won!",
                f"Congratulations!\nThe word was: {self.word}"
            )
            self.disable_buttons()

        # Check lose
        elif self.wrong_guesses >= self.max_wrong:
            messagebox.showerror(
                "❌ Game Over",
                f"You lost!\nThe word was: {self.word}"
            )
            self.disable_buttons()

    def update_display(self):
        display = ""

        for letter in self.word:
            if letter in self.guessed:
                display += letter + " "
            else:
                display += "_ "

        self.word_label.config(text=display)

        remaining = self.max_wrong - self.wrong_guesses

        self.attempts_label.config(
            text=f"❤️ Attempts remaining: {remaining}"
        )

        if self.guessed:
            letters = ", ".join(sorted(self.guessed))
            self.guessed_label.config(
                text=f"Guessed letters: {letters}"
            )
        else:
            self.guessed_label.config(
                text="Guessed letters: None"
            )

    def disable_buttons(self):
        for button in self.buttons.values():
            button.config(state=tk.DISABLED)


# Start the application
root = tk.Tk()
game = HangmanGame(root)
root.mainloop()