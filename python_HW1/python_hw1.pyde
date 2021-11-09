"""
Homework 1
15. 10. 2021

Artist description
Text + pic on screen

"""

overButton = False

def setup():
    size(800, 500)
    background(204)
    global img, about
    
    f = createFont("Georgia", 18)
    textFont(f)
    
    img = loadImage("Artdanion_profil_small_k.png")
    about = loadStrings("/data/about.txt")

    
    lineCount=height/4 * width/4
    
    for i in range(lineCount):
        stroke(color(random(255),random(255),random(255)))
        line(random(width), random(height), random(width), random(height))
    
def draw():
    
    margin = 10
    gap = 46
    counter = 35
    
    translate(margin * 4, margin * 4)
        
    stroke(255,255,255)
    fill(150, 10)
    rect(0, 0 ,width-(margin * 8),height-(margin * 8))
    
    translate(margin * 2, margin * 2)
    image(img, 430, 0, 250, 250)
    
    fill(0)
    x=0
        
    for zeile in about:
        text(zeile, 0, 10+x, 400, 500)
        x=x+200
        
    if overButton:
        fill(255)
    else:
        noFill()
    
    rect(430, 295, 210, 40)
    fill(0)
    text("www.daniel-fischer.at", 450,320)


def mousePressed():
    if overButton:
        link("https://www.daniel-fischer.at")


def mouseMoved():
    checkButtons()


def mouseDragged():
    checkButtons()


def checkButtons():
    global overButton
    overButton = 460 < mouseX < 700 and 350 < mouseY < 400;
