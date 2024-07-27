import tkinter as tk
from tkinter import messagebox
import random

class MastermindGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Mastermind Game")

        self.colors = ["red", "green", "yellow", "blue", "purple", "orange"]
        self.code_length = 2
        self.max_attempts = 5

        self.code = random.choices(self.colors, k=self.code_length)
        self.attempts = 0

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        self.info_label = tk.Label(self.master, text=f"Available colors: {', '.join(self.colors)}\n"
                                                      f"Code length: {self.code_length}, Max attempts: {self.max_attempts}",
                                  font=('Arial', 12))
        self.info_label.pack(pady=10)

        self.guess_label = tk.Label(self.master, text=f"Enter your guess (space-separated, {self.code_length} colors):", font=('Arial', 12))
        self.guess_label.pack(pady=5)

        self.guess_entry = tk.Entry(self.master, font=('Arial', 12))
        self.guess_entry.pack(pady=5)

        self.submit_button = tk.Button(self.master, text="Submit Guess", command=self.check_guess, font=('Arial', 12))
        self.submit_button.pack(pady=10)

        self.result_text = tk.Text(self.master, height=10, width=50, font=('Arial', 12))
        self.result_text.pack(pady=10)

    def check_guess(self):
        guess = self.guess_entry.get().strip().split()

        if len(guess) != self.code_length or not all(color in self.colors for color in guess):
            messagebox.showerror("Invalid Guess", f"Make sure you have exactly {self.code_length} colors from the available options.")
            return

        self.attempts += 1
        correct_position = sum(g == c for g, c in zip(guess, self.code))
        correct_color = sum(min(guess.count(c), self.code.count(c)) for c in set(self.code))
        correct_color -= correct_position

        self.result_text.insert(tk.END, f"Attempt {self.attempts}/{self.max_attempts}: {guess}\n")
        self.result_text.insert(tk.END, f"{correct_position} colors placed correctly!\n")
        self.result_text.insert(tk.END, f"{correct_color} correct colors placed in wrong position\n\n")
        self.guess_entry.delete(0, tk.END)

        if correct_position == self.code_length:
            messagebox.showinfo("Congratulations", "Congratulations! You won!")
            self.master.quit()
        elif self.attempts >= self.max_attempts:
            messagebox.showinfo("Game Over", "Sorry, you have lost!")
            self.master.quit()

if __name__ == "__main__":
    root = tk.Tk()
    game = MastermindGame(root)
    root.mainloop()
