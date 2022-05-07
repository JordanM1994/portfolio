from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

fonts = {
    "Goldman": "Goldman-Regular.ttf",
    "Inconsolata": "Inconsolata-Regular.ttf",
    "WorkSans": "WorkSans-Regular.ttf"
}

positions = ["Top", "Bottom"]


def watermarking():

    photo = Image.open(upload_file_link.cget("text"))

    w, h = photo.size
    print(w, h)

    drawing = ImageDraw.Draw(photo)
    font = ImageFont.truetype(f'fonts/{fonts[font_clicked.get()]}', 40)

    text = text_box.get()
    text_w, text_h = drawing.textsize(text, font)

    if pos_clicked.get() == "Top":
        pos = (0, 0)
    elif pos_clicked.get() == "Bottom":
        pos = (0, h-50)

    c_text = Image.new('RGB', (text_w, (text_h)), color = '#000000')
    drawing = ImageDraw.Draw(c_text)

    drawing.text((0,0), text, fill="#ffffff", font=font)
    c_text.putalpha(100)

    photo.paste(c_text, pos, c_text)
    photo.save('watermarked_images/watermarked_image.png')

    messagebox.showinfo(title="Success", message="Your image has been successfully watermarked.")
    img.config(file="watermarked_images/watermarked_image.png")

def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    upload_file_link.config(text=filename)


window = Tk()
window.title("Watermarker")
window.config(padx=100, pady=50)

canvas = Canvas(width=200, height=224, highlightthickness=0)
img = PhotoImage(file="")
canvas.create_image(100, 112, image=img)
canvas.grid(column=0, row=0, columnspan=2)

upload_file_label = Label(text="Please select a file to upload")
upload_file_label.grid(column=0,row=1)
upload_file = Button(window, text='Open', command=UploadAction)
upload_file.grid(column=1,row=1)
upload_file_link = Label(text="")
upload_file_link.grid(column=0,row=2, columnspan=2)

text_label = Label(text="What text would you like to set?")
text_label.grid(column=0, row=3)
text_box = Entry()
text_box.grid(column=1, row=3)
text_box.focus()

font_clicked = StringVar()
font_clicked.set("Goldman")

font_selection_label = Label(text="What font would you like to use?")
font_selection_label.grid(column=0, row=4)
font_selection_dropdown = OptionMenu(window, font_clicked ,*fonts.keys())
font_selection_dropdown.grid(column=1, row=4)

pos_clicked = StringVar()
pos_clicked.set("Top")

pos_selection_label = Label(text="What font would you like to use?")
pos_selection_label.grid(column=0, row=5)
pos_selection_dropdown = OptionMenu(window, pos_clicked ,*positions)
pos_selection_dropdown.grid(column=1, row=5)

submit = Button(text="Watermark!", command=watermarking)
submit.grid(column=0, row=6, columnspan=2)


success_message = Label(text="")
success_message.grid(column=0,row=7, columnspan=2)

window.mainloop()
