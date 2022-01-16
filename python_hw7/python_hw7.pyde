"""
Homework 7
Copyright (C) 2022 Daniel Fischer
www.daniel-fischer.at
14. 01. 2022

Art description
glitch effects / with filters or spliting color channels r/ g / b

picture credit: NASA see https://www.nasa.gov/multimedia/guidelines/index.html
copied from: https://fr.wikipedia.org/wiki/Fichier:Sydney,_Australia_-_Flickr_-_NASA_Goddard_Photo_and_Video.jpg

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

import time

def setup():
    size(1000, 1000) #1200x1200 gives better result
    global img, imgR, imgG, imgB
    img = loadImage("earth_600px.jpg")    # Load an image into the program
    
    imgR = createImage(img.width, img.height, ARGB)
    pixCount = len(imgR.pixels)
    for i in range(pixCount):
        pixR = img.pixels[i]
        r = red(pixR)
        r = int(round(r/255)) * 255
        imgR.pixels[i] = color(r, 0, 0, 200)

    imgG = createImage(img.width, img.height, ARGB)
    pixCount = len(imgR.pixels)
    for i in range(pixCount):
        pixG = img.pixels[i]
        g = red(pixG)
        g = int(round(g/255)) * 255
        imgG.pixels[i] = color(0, g, 0, 200)
        
    imgB = createImage(img.width, img.height, ARGB)
    pixCount = len(imgB.pixels)
    for i in range(pixCount):
        pixB = img.pixels[i]
        b = blue(pixB)
        b = int(round(b/255)) * 255
        imgB.pixels[i] = color(0, 0, b, 200)
    
    background(0,0,0)

def draw():
    tint(255, 126)
    image(img, 0, 0)
    image(imgR, width/2, 0)
    image(imgG, 0, height/2)
    image(imgB, width/2, height/2)
    
    if mousePressed:
        tint(255,0,0, random(200))
        image(img,  (width/4)+random(-10, 10), (height/4)+random(-10, 10))
        #filter(DILATE)
        tint(0,255,0, random(200))
        image(img, (width/4)+random(-10, 10), (height/4)+random(-10, 10))
        #filter(DILATE)
        tint(0,0,255, random(200))
        image(img, (width/4)+random(-10, 10), (height/4)+random(-10, 10))
        #filter(DILATE)
        time.sleep(0.1)
        #saveFrame("screenshot.jpg")
  
    else:
        background(0,0,0)
        tint(255, 255)
        image(img, width/4, height/4)
        
