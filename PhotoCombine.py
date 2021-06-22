
from PIL import Image, ImageFilter, ImageFont, ImageDraw
from random import randrange

def getTextArry(textFileName):
    textArray = []
    file = open(textFileName, "r", encoding="utf-8")
    for line in file:
        textArray.append(line.strip())

    return textArray

def getThePhoto():
    #rnadrange(2) => 0,1,2
    path = "photo/" + str(randrange(6) + 1) + '.jpg'
    return Image.open(path)

def textNextLine(text):
    textLine = ""
    i = 0
    while i <= len(text):
        textLine = textLine + text[i:i+7] + '\n'
        i += 7
    return textLine

def generatePhoto():
    textFile = "TextFile/famous.txt"
    textArray = getTextArry(textFile)
    my_image = getThePhoto()
    #Image Effect
    my_image = my_image.filter(ImageFilter.GaussianBlur(radius = 5))
    text = textArray[randrange(25)]
    text = textNextLine(text)
    #Text position
    textSize = 150
    width, height = my_image.size
    x = 75
    y = (height - textSize * text.count('\n') + textSize)/2
    font = ImageFont.truetype(font="textStyle/NotoSerifCjktc-Black.otf",size=textSize)
    drawer = ImageDraw.Draw(my_image)

    fill_color = (255, 255, 255)
    stroke_color = (131, 131, 131)

    drawer.text((x, y), text, font=font, fill=fill_color, stroke_width=3, stroke_fill=stroke_color)
    my_image.save('out_put_photo/result.jpg')
    return my_image
    
if __name__ == "__main__":
    my_image = generatePhoto()
