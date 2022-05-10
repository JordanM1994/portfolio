from tkinter import *
from tkinter import filedialog, messagebox
from sentences import sentences
import random
import time

heading_font = ("fonts/SourceCodePro-Medium.ttf", 50)
copy_text_font = ("fonts/SourceCodePro-LightItalic.ttf", 20)
user_text_font = ("fonts/SourceCodePro-Light.ttf", 15)

start = time.time()

def stop_timer():
    stop = time.time()
    print("The time of the run:", stop - start)


def collect_data(event=None):
    stop = time.time()
    print("The time of the run:", stop - start)
    correct_words = 0
    users_typing = user_input.get().split(" ")
    random_words = random_sentence.split(" ")
    for n in range(0,len(random_words)):
        if users_typing[n] == random_words[n]:
            correct_words += 1
        else:
            pass
    return print(correct_words)


random_sentence = random.choice(sentences)

window = Tk()
window.title("Typing Speed Test")
window.config(padx=50, pady=50, background="black")

title_label = Label(text="Type Speed Test", pady=50, background="black", foreground="blue", font=heading_font)
title_label.grid(column=0,row=0)

copy_text = Label(text=f"{random_sentence}", background="black", foreground="white", font=copy_text_font, pady=100)
copy_text.grid(column=0,row=1)

user_input = Entry(background="black", foreground="white", font=user_text_font, width=100, highlightcolor="yellow", highlightthickness=3)
user_input.grid(column=0, row=2)
user_input.focus()

window.bind('<Return>',collect_data)

window.mainloop()
