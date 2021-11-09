"""
Copyright (C) Daniel Fischer 2021
Homework 3 - Programming I (380.005) / Interface Cultures
26. 10. 2021

picture credit:
    opolka.jpg    photo - PAP               http://archiwum.thenews.pl/1/11/Artykul/190389
    flower.jpg    Michellejo (CC BY 3.0)    https://en.wikipedia.org/wiki/File:Oxalis_tetraphylla_flower.jpg
    
"""

#configure

textsize = 10
count = 840
line_gap = 2
margin_right = 5
margin_left = 5

pic = True

def setup():
    size(800,600)
    background(0)
    
    
    f = createFont("Georgia", textsize)
    textFont(f)
    imageMode(CENTER)
    
    output = "0 " 
       
    #creating an arry with binary numbers
    for i in range(1, int(count), 1):
            output += decimalToBinary(i)+ " "
       
    fill(255)
    x=margin_left
    y=textsize
    
    #printing the arry on the screen
    for j in range(0, len(output), 1):
        text(output[j],x,y)
        x += textWidth(output[j])
        if x > width-margin_right:
            y += textsize+line_gap
            x = 0
    
    #storing the picture as an alphamask
    saveFrame("mask.jpg")
    
    
def draw():
    global pic, img, imgMask
    
    #displaying image 1 or 2 on screen and appling alpha mask   
    if pic:
        imgMask = loadImage("mask.jpg")
        img = loadImage("opolka.jpg")
        img.mask(imgMask)
        image(img, width / 2, height / 2)
        #saveFrame("HW3_pic1.jpg")
    else:
        img = loadImage("flower.jpg")
        img.mask(imgMask)
        image(img, width / 2, height / 2)
        #saveFrame("HW3_pic2.jpg")
    
    
    
def decimalToBinary(n):
    
    # DEC --> BIN
    return bin(n).replace("0b", "")


def keyPressed():
    
    #detecting left or right arrow key to switch images
    global pic
    if (key == CODED):
        if (keyCode == LEFT) or (keyCode == RIGHT):
            clear()
            pic = not pic
