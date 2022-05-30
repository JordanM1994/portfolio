from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# ------------------------------------------ Colours -------------------------------------------#

BACKGROUND = "white"
TEXT_COLOUR = "black"

# ------------------------------------------ fonts -------------------------------------------#

# This dictionary is used to create the dropdown list of fonts that correlate to the fonts in the fonts folder
# TODO 2 - Choose better fonts for the user to use.

fonts = {
    "Goldman": "Goldman-Regular.ttf",
    "Inconsolata": "Inconsolata-Regular.ttf",
    "WorkSans": "WorkSans-Regular.ttf",
}

# ------------------------------------------ Watermark position -------------------------------------------#

# This list is used to create the dropdown list of positions
positions = ["Top", "Bottom"]

# --------------------------------------------- Alignment  ---------------------------------------------------#

# This list is used to create the dropdown list of alignments
alignments = ["Left", "Center", "Right"]

# --------------------------------------------- Font size  ---------------------------------------------------#

# This list is used to create the dropdown list of Font Sizes
font_size = ["Small", "Medium", "Large"]

# ------------------------------------------ watermarking function -------------------------------------------#


def watermarking():

    # opens the image file that will be watermarked
    if upload_file_link.cget("text") == "":
        messagebox.showerror(title="Error", message="Please select an image to add a watermark too.")
    else:
        photo = Image.open(upload_file_link.cget("text"))

        # gathers the image's height and width
        w, h = photo.size

        # determines the size of the text due
        if font_size_clicked.get() == "Small":
            font_size = 15
        elif font_size_clicked.get() == "Medium":
            font_size = 30
        elif font_size_clicked.get() == "Large":
            font_size = 50

        # 'draws' the photo onto a black canvas
        drawing = ImageDraw.Draw(photo)
        watermark_font = ImageFont.truetype(f'fonts/{fonts[font_clicked.get()]}', font_size)

        # creates the text box for the watermark text
        text = text_box.get()
        if text == "":
            messagebox.showerror(title="Error", message="There isn't any text to use as a Watermark, please enter text you"
                                                       " would like to show on the image.")
            pass
        else:
            text_w, text_h = drawing.textsize(text, watermark_font)

            # defines the center/right x value for the text ot be used in the if statement below
            center_text = int(w/2)-int(text_w/2)
            right_text = w-text_w

            # if statement to check if the user wants the watermark at the top or bottom of the image and assigns the correct
            # there is then an embedded if statement to identify the alignment of the text on the
            # x and y coordinates
            if pos_clicked.get() == "Top":
                if align_clicked.get() == "Left":
                    pos = (0, 0)
                elif align_clicked.get() == "Center":
                    pos = (center_text, 0)
                elif align_clicked.get() == "Right":
                    pos = (right_text, 0)
            elif pos_clicked.get() == "Bottom":
                if align_clicked.get() == "Left":
                    pos = (0, h-text_h)
                elif align_clicked.get() == "Center":
                    pos = (center_text, h-text_h)
                elif align_clicked.get() == "Right":
                    pos = (right_text, h-text_h)

            # creates the black background colour for the text
            c_text = Image.new('RGB', (text_w, text_h), color='#000000')
            drawing = ImageDraw.Draw(c_text)

            # draws the white text onto the image
            drawing.text((0, 0), text, fill="#ffffff", font=watermark_font)
            c_text.putalpha(100)

            photo.paste(c_text, pos, c_text)

            # TODO 1 - Allow the user to preview the image and then save once they are happy.

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

# window creates the TKinter window and names it "Watermark" and sets the padding on the x and y axis
window = Tk()
window.title("Watermarker")
window.config(padx=100, pady=50, background=BACKGROUND)

# Upload file label and button to allow the user to choose the image they would like to watermark
upload_file_label = Label(text="Please select a photo to upload", background=BACKGROUND, foreground=TEXT_COLOUR)
upload_file_label.grid(column=0, row=1)
upload_file = Button(window, text='Open', command=upload_action, background=BACKGROUND)
upload_file.grid(column=1, row=1)
upload_file_link = Label(text="", background=BACKGROUND, foreground=TEXT_COLOUR)
upload_file_link.grid(column=0, row=2, columnspan=2)

# TODO 3 - make this text field a mandatory field, show ! when empty
# Text label and text box allows the user to enter the text that they want to add as the watermark
text_label = Label(text="Watermark Text", background=BACKGROUND, foreground=TEXT_COLOUR, pady=10)
text_label.grid(column=0, row=3)
text_box = Entry(background=BACKGROUND)
text_box.grid(column=1, row=3)
text_box.focus()

# Allows the user to choose a font from a dropdown lost
font_clicked = StringVar()
font_clicked.set("Goldman")


font_selection_label = Label(text="Font", background=BACKGROUND, foreground=TEXT_COLOUR, pady=10)
font_selection_label.grid(column=0, row=4)
font_selection_dropdown = OptionMenu(window, font_clicked, *fonts.keys())
font_selection_dropdown.config(background=BACKGROUND)
font_selection_dropdown.grid(column=1, row=4)

# Allows the user to choose the position of the watermark from a dropdown lost
pos_clicked = StringVar()
pos_clicked.set("Top")

pos_selection_label = Label(text="Position", background=BACKGROUND, foreground=TEXT_COLOUR, pady=10)
pos_selection_label.grid(column=0, row=5)
pos_selection_dropdown = OptionMenu(window, pos_clicked, *positions)
pos_selection_dropdown.config(background=BACKGROUND)
pos_selection_dropdown.grid(column=1, row=5)

# Allows the user to choose the alignment of the watermark from a dropdown lost
align_clicked = StringVar()
align_clicked.set("Left")

align_selection_label = Label(text="Alignment", background=BACKGROUND, foreground=TEXT_COLOUR, pady=10)
align_selection_label.grid(column=0, row=6)
align_selection_dropdown = OptionMenu(window, align_clicked, *alignments)
align_selection_dropdown.config(background=BACKGROUND)
align_selection_dropdown.grid(column=1, row=6)

# Allows the user to choose the font size of the watermark from a dropdown lost
font_size_clicked = StringVar()
font_size_clicked.set("Small")

font_size_selection_label = Label(text="Font size", background=BACKGROUND, foreground=TEXT_COLOUR, pady=10)
font_size_selection_label.grid(column=0, row=7)
font_size_selection_dropdown = OptionMenu(window, font_size_clicked, *font_size)
font_size_selection_dropdown.config(background=BACKGROUND)
font_size_selection_dropdown.grid(column=1, row=7)


# Submit button that calls the "Watermarking()" function
submit = Button(text="Watermark!",
                command=watermarking,
                background=BACKGROUND,
                foreground=TEXT_COLOUR
                )
submit.grid(column=0, row=9, columnspan=2)

success_message = Label(text="")
success_message.grid(column=0, row=10, columnspan=2)

window.mainloop()
