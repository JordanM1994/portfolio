from tkinter import *
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
        self.total_time = 0
        self.correct_words = 0
        self.wpm = 0
        self.accuracy = 0
        self.correct_letters = 0


    def start_game(self, event=None):
        copy_text.config(text=f"{random.choice(sentences)}")
        user_input.focus()
        self.start = time.time()
        window.bind('<Return>', self.collect_data)


    def collect_data(self, event=None):
        self.finish = time.time()
        self.users_typing = user_input.get("1.0", END).split(" ")
        self.random_words = copy_text.cget("text").split(" ")

        for n in range(0, len(self.random_words)):
            try:
                if "\n" in self.users_typing[n-1]:
                    if self.users_typing[n-1].replace("\n", "") == self.random_words[n-1]:
                        self.correct_words += 1
                    else:
                        pass
                elif self.users_typing[n-1] == self.random_words[n-1]:
                    self.correct_words += 1
                else:
                    pass
            except IndexError:
                pass

        self.users_typing_letters = list(user_input.get("1.0", END))
        self.random_words_letters = list(copy_text.cget("text"))


        for n in range(len(self.users_typing_letters)):
            if self.users_typing_letters[n-1] == self.random_words_letters[n-1]:
                self.correct_letters += 1
            else:
                pass

        self.accuracy = int((self.correct_letters/len(self.users_typing_letters))*100)

        self.total_time = int(self.finish - self.start)
        self.wpm = self.correct_words/(self.total_time/60)
        self.results = Label(text=f"time: {int(self.finish - self.start)} seconds   accuracy:{self.accuracy}%    wpm: {int(self.wpm)}",
                        pady=50, background="black", foreground="blue", font=copy_text_font)
        self.results.grid(columnspan=2, column=0, row=3)
        self.restart = Button(text="Try again", command=self.clear)
        self.restart.grid(columnspan=2, column=0, row=4)


    def clear(self):
        self.results.grid_remove()
        self.restart.grid_remove()
        user_input.delete(1.0,END)
        self.start_game()


window = Tk()
window.title("Typing Speed Test")
window.config(padx=50, pady=50, background="black")
title_label = Label(text="Type Speed Test", pady=50, background="black", foreground="blue", font=heading_font)
title_label.grid(column=0, row=0)

copy_text = Label(text="", background="black", foreground="white", font=copy_text_font,
                     pady=100)
copy_text.grid(column=0, row=1)

user_input = Text(background="black", foreground="white", font=user_text_font, width=100,
                      highlightcolor="yellow", highlightthickness=3, height=2)
user_input.grid(column=0, row=2)


game = TypingSpeedTest()
game.start_game()

window.mainloop()
