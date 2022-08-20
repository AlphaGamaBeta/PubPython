from PIL import Image, ImageDraw, ImageFont

image = Image.open('IMG.jpg').convert("RGBA")
draw = ImageDraw.Draw(image)
text = "Input the water mark: "
font = ImageFont.truetype('arial.ttf', 50)
width, height = image.size
x = width / 4
y = height / 12

draw.text((x, y), text, font=font, fill=(255, 255, 255, 100))
image.show()

image.save('imgwatermark.jpg')