from tkinter import *
from tkinter import filedialog, messagebox
from sentences import sentences
import random
import time


start = time.time()

def stop_timer():
    stop = time.time()
    print("The time of the run:", stop - start)


window = Tk()
window.title("Typing Speed Test")

button = Button(text="Click", command=stop_timer)
button.grid(column=0, row=0)
#
# random_sentence = random.choice(sentences)
# print(random_sentence)



window.mainloop()
