from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# ------------------------------------------ fonts -------------------------------------------#

# This dictionary is used to create the dropdown list of fonts that correlate to the fonts in the fonts folder
fonts = {
    "Goldman": "Goldman-Regular.ttf",
    "Inconsolata": "Inconsolata-Regular.ttf",
    "WorkSans": "WorkSans-Regular.ttf",
}

# ------------------------------------------ Watermark position -------------------------------------------#

# This dictionary is used to create the dropdown list of positions
positions = ["Top", "Bottom"]

# ------------------------------------------ watermarking function -------------------------------------------#


def watermarking():

    # opens the image file that will be watermarked
    photo = Image.open(upload_file_link.cget("text"))

    # gathers the image's height and width
    w, h = photo.size

    # 'draws' the photo onto a black canvas
    drawing = ImageDraw.Draw(photo)
    watermark_font = ImageFont.truetype(f'fonts/{fonts[font_clicked.get()]}', 40)

    # creates the text box for the watermark text
    text = text_box.get()
    text_w, text_h = drawing.textsize(text, watermark_font)

    # if statement to check if the user wants the watermark at the top or bottom of the image and assigns the correct
    # x and y coordinates
    if pos_clicked.get() == "Top":
        pos = (0, 0)
    elif pos_clicked.get() == "Bottom":
        pos = (0, h-50)

    # creates the black background colour for the text
    c_text = Image.new('RGB', (text_w, text_h), color='#000000')
    drawing = ImageDraw.Draw(c_text)

    # draws the white text onto the image
    drawing.text((0, 0), text, fill="#ffffff", font=watermark_font)
    c_text.putalpha(100)

    photo.paste(c_text, pos, c_text)

    # saves the image to the location below
    photo.save('watermarked_images/watermarked_image.png')

    # alerts the user letting them know the watermark was successful
    messagebox.showinfo(title="Success", message="Your image has been successfully watermarked.")

    # ----------------------- Preview Image -----------------------------------------------#

    # sets the canvas width and height relative to the uploaded image
    canvas_width = w+100
    canvas_height = h+50

    # adds the image to the app and displays it at the top
    canvas = Canvas(width=canvas_width, height=canvas_height, highlightthickness=0)
    img = PhotoImage(file="")
    canvas.create_image(canvas_width / 2, canvas_height / 2, image=img)
    canvas.grid(column=0, row=0, columnspan=2)

    img.config(file="watermarked_images/watermarked_image.png")


# ------------------------------------------ watermarking function -------------------------------------------#

# this function is used by the "open" button to allow the user to locate the image they want watermarked and upload
def upload_action():
    filename = filedialog.askopenfilename()
    upload_file_link.config(text=filename)

# ------------------------------------------ watermarking function -------------------------------------------#


window = Tk()
window.title("Watermarker")
window.config(padx=100, pady=50)

upload_file_label = Label(text="Please select a photo to upload")
upload_file_label.grid(column=0, row=1)
upload_file = Button(window, text='Open', command=upload_action)
upload_file.grid(column=1, row=1)
upload_file_link = Label(text="")
upload_file_link.grid(column=0, row=2, columnspan=2)

text_label = Label(text="Watermark Text")
text_label.grid(column=0, row=3)
text_box = Entry()
text_box.grid(column=1, row=3)
text_box.focus()

font_clicked = StringVar()
font_clicked.set("Goldman")

font_selection_label = Label(text="Font")
font_selection_label.grid(column=0, row=4)
font_selection_dropdown = OptionMenu(window, font_clicked, *fonts.keys())
font_selection_dropdown.grid(column=1, row=4)

pos_clicked = StringVar()
pos_clicked.set("Top")

pos_selection_label = Label(text="Position")
pos_selection_label.grid(column=0, row=5)
pos_selection_dropdown = OptionMenu(window, pos_clicked, *positions)
pos_selection_dropdown.grid(column=1, row=5)

submit = Button(text="Watermark!", command=watermarking)
submit.grid(column=0, row=6, columnspan=2)

success_message = Label(text="")
success_message.grid(column=0, row=7, columnspan=2)

window.mainloop()
