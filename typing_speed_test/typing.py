from tkinter import *
from tkinter import filedialog, messagebox
from sentences import sentences
import random
import time

heading_font = ("fonts/SourceCodePro-Medium.ttf", 50)
copy_text_font = ("fonts/SourceCodePro-LightItalic.ttf", 20)
user_text_font = ("fonts/SourceCodePro-Light.ttf", 15)

class TypingSpeedTest:

    def __init__(self):
        self.start = 0
        self.finish = 0
        self.correct_words = 0


    def start_game(self, event=None):
        self.copy_text = Label(text=f"{random.choice(sentences)}", background="black", foreground="white", font=copy_text_font,
                          pady=100)
        self.copy_text.grid(column=0, row=1)

        self.user_input = Text(background="black", foreground="white", font=user_text_font, width=100,
                           highlightcolor="yellow", highlightthickness=3, height=2)
        self.user_input.grid(column=0, row=2)
        self.user_input.focus()
        self.start = time.time()

        window.bind('<Return>', self.collect_data)


    def collect_data(self, event=None):
        self.finish = time.time()
        users_typing = self.user_input.cget("text").split(" ")
        random_words = self.copy_text.cget("text").split(" ")
        for n in range(0, len(random_words)):
            if users_typing[n] == random_words[n]:
                self.correct_words += 1
            else:
                pass
        results = Label(text=f"time: {int(self.finish - self.start)} seconds   correct words: {self.correct_words}",
                        pady=50, background="black", foreground="blue", font=copy_text_font)
        results.grid(columnspan=2, column=0, row=3)
        restart = Button(text="Try again")
        restart.grid(columnspan=2, column=0, row=4)


window = Tk()
window.title("Typing Speed Test")
window.config(padx=50, pady=50, background="black")
title_label = Label(text="Type Speed Test", pady=50, background="black", foreground="blue", font=heading_font)
title_label.grid(column=0, row=0)

game = TypingSpeedTest()
game.start_game()

window.mainloop()
