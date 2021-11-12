"""
Homework 4
Copyright (C) 2021 Daniel Fischer
www.daniel-fischer.at
11. 11. 2021

Art description
b/w animation on screen

tree_BW.svg Copyright Daniel Fischer 2021
full-moon-clipart-black-and-white.jpg from https://clipartstation.com/full-moon-clipart-black-and-white/

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

overButton = False

def setup():
    frameRate(60)
    size(1000, 800)
    global img_tree, img_moon, img_bars, bird, center_x, center_y, x, y, angle, radius
    global movex, movey
    
    radius = 20
    angle = 1
    center_x = width/4 +300
    center_y = height/2
    movex = height
    movey = width
    
    img_bars = loadImage("bars.png")
    img_tree = loadImage("tree_BW.png")
    img_moon = loadImage("full-moon-clipart-black-and-white.jpg")
    bird = loadShape("bird_BW.svg") 
    
def draw():
    background(250)
    global img_tree, img_moon, bird, center_x, center_y, x, y, angle
    global movex, movey
    
    x = center_x + cos(angle)*radius
    y = center_y + sin(angle)*radius
    angle += PI/60
    
    push()
    translate(x, y)
    rotate(-angle/2)
    shape(bird, 10, 10, y, y)
    pop()
    
    push()
    translate(x, y)
    rotate(-angle/4)
    shape(bird, 40, 10, x, x)
    pop()
    
    image(img_moon, 650, 50, 110, 110)
    image(img_tree, 110, 100, 500, 700)
    
    if movex > 520:
        movex = movex-1
    if movey > 620:
        movey = movey-1
        
    image(img_bars, 0, -movex+height+height/2)
    image(img_bars, 0, movex-(height+height/2))
    
    push()
    rotate(PI/2.0)
    image(img_bars, -100, -movey+width/2)
    image(img_bars, -100, movey-(2*width+width/2)+200)
    pop()
    
    #saveFrame("screenshot.jpg")
    
