from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

photo = Image.open("images/photo-1.jpg")

w, h = photo.size
print(w, h)

drawing = ImageDraw.Draw(photo)
font = ImageFont.truetype('fonts/WorkSans-Regular.ttf', 68)

text = "© Jordan McLeod "
text_w, text_h = drawing.textsize(text, font)

pos = w - text_w, (h - text_h) - 50

c_text = Image.new('RGB', (text_w, (text_h)), color = '#000000')
drawing = ImageDraw.Draw(c_text)

drawing.text((0,0), text, fill="#ffffff", font=font)
c_text.putalpha(100)

photo.paste(c_text, pos, c_text)
photo.save('watermarked_images/watermarked_image.jpg')