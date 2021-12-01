"""
Homework 6
Copyright (C) 2021 Daniel Fischer
www.daniel-fischer.at
20. 11. 2021

Art description
b/w text animation on screen / with classes and vectors

text: William Shakespeare,
http://shakespeare.mit.edu/Poetry/sonnet.LX.html

Sonnets, LX:
Like as the waves make towards the pebbl'd shore,
So do our minutes hasten to their end;
Each changing place with that which goes before,
In sequent toil all forwards do contend.
Nativity, once in the main of light,
Crawls to maturity, wherewith being crown'd,
Crooked eclipses 'gainst his glory fight,
And Time that gave doth now his gift confound.
Time doth transfix the flourish set on youth
And delves the parallels in beauty's brow,
Feeds on the rarities of nature's truth,
And nothing stands but for his scythe to mow:
And yet to times in hope my verse shall stand,
Praising thy worth, despite his cruel hand.
"""

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


def setup():
    
    frameRate(60)
    size(600, 600)
    global poem, poem_lines, font, xPos, yPos, maxY, speed, line_Height, gap, zeilen_count, num_zeile, left, zeile, zeichen, line_cursor, finished
    
    poem = []
    num_zeile = []
    
    left = 85
    maxY = 100
    speed = 10
    line_Height = 20
    gap = 5
    
    xPos = left
    yPos = 0
    line_cursor = 0
    zeile = 0
    zeichen = 0
    finished = False
          
    poem_lines = []
    # list of lines
    with open('data/shakespear.txt') as f:
        poem_lines = f.readlines()
        
    # counts lines in the poem
    zeilen_count = len(poem_lines)
    
    # list of line lenght
    for i in xrange(zeilen_count):
        num_zeile.append(len(poem_lines[i]))
    
    # defines font with font size lineHeight     
    font = createFont("Arial", line_Height, True)
    textFont(font)
    fill(0)
    
    # first letter add
    poem.append(Letter(xPos, yPos, poem_lines[0][0]))
  
def draw():
    println(frameRate)
    #draw gradient
    gradient(3*width/4, 0, width/2, height, 240, 0)
  
    global poem, poem_lines, font, xPos, yPos, maxY, speed, line_Height, gap, left, zeile, zeichen, line_cursor
    
    #draw actual character falling / no spaces
    if maxY > poem[zeichen].y:
        if poem[zeichen] != ' ':
            poem[zeichen].update()
        else:
            poem[zeichen].y =maxY
    else:
        if line_cursor < num_zeile[zeile]-1:# next character added
            zeichen += 1
            xPos += textWidth(poem[zeichen-1].letter)
            yPos = 0
            line_cursor += 1
            poem.append(Letter(xPos, yPos, poem_lines[zeile][line_cursor]))
        else: 
            if zeile < zeilen_count-1:# next line added
                zeile += 1
                line_cursor = 0
                xPos = left
                yPos = 0
                maxY += line_Height + gap               
                poem.append(Letter(xPos, yPos, poem_lines[zeile][line_cursor]))
                zeichen +=1
            else:
                finished = True

    # drawing all added characters        
    for i in xrange(len(poem)):
        poem[i].display()

            
# function to draw gradients
def gradient(x, y, w, h, color1, color2):
    
    for i in xrange((x+w)):
        inter = map(i, x, x+w, 0, 1)
        c = lerpColor(color1, color2, inter)
        stroke(c)
        line(i, y, i, y+h)

# A class to describe a single Letter
class Letter():
    global speed, maxY
    
    def __init__(self, x, y, letter):
        self.backx = self.x = x
        self.backy = self.y = y
        self.letter = letter
        
    def update(self):
        fspeed = speed # fspeed increases over duration --> letters have acceleration
        if (self.y + speed) < maxY:
           self.y += fspeed
           self.backy =self.y
           fspeed += 5
        else:
           self.y = maxY
           self.backy = self.y
           fspeed = speed

    # Display the Letter
    def display(self):
        textAlign(LEFT)
        
        location = PVector(self.x, self.y)
        velocity = PVector(random(-3, 3), random(-3, 3))
        mouseLocation = PVector(mouseX, mouseY)
        abstossung = PVector.sub(location, mouseLocation)
        # vectors for location, mouselocation, velocity and force
        # force vector --> vector mouse to position --> normalized + multiplied by magnitutde (maped 50 --> 2 - 0)
        # and added to velocity
        # --> this added to location
        
        distanceToM = abstossung.mag()

        if distanceToM < 50:
            abstossung.normalize()
            abstossung.mult(map(distanceToM, 0, 50, 2, 0))
            velocity.add(abstossung)
            location.add(velocity)
            self.x = location.x
            self.y = location.y
        else:
            self.x = self.backx
            self.y = self.backy
 
        text(self.letter, self.x, self.y)
