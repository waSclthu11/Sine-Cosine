"""
sinecosine.py
Author: waSclthu11
Credit: tutorial and info in assignment github.

Assignment:

In this assignment you must use *list comprehensions* to generate sprites that show the behavior
of certain mathematical functions: sine and cosine. 

The sine and cosine functions are provided in the Python math library. These functions are used
to relate *angles* to *rectangular* (x,y) coordinate systems and can be very useful in computer
game design.

Unlike the last assignment using ggame`, this one will not provide any "skeleton" code to fill
in. You should use your submission for the Picture assignment 
(https://github.com/HHS-IntroProgramming/Picture) as a reference for starting this assignment. 

See:
https://github.com/HHS-IntroProgramming/Sine-Cosine/blob/master/README.md
for a detailed list of requirements for this assignment.

https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Displaying-Graphics
for general information on how to use ggame.

https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Programmed-Graphics
for general information on using list comprehensions to generate graphics.

http://brythonserver.github.io/ggame/
for detailed information on ggame.
"""
from math import sin, cos, radians
from ggame import App, Color, LineStyle, Sprite
from ggame import CircleAsset

red = Color(0xff0000, 1.0)
purple = Color(0x800080, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
a = 360
thinline = LineStyle(1, black)
bluecircle = CircleAsset(5, thinline, blue)
purplecircle = CircleAsset(5, thinline, purple)
redcircle = CircleAsset(5, thinline, red)
xval = range(0, a, 10)


ybluecoordinates = [(100 + 100*sin(radians(x))) for x in range(0, a, 10)]
#ybluecoordinates = 100+100*sin(radians(xval))
yredcoordinates = [(100+100*cos(radians(x))) for x in range(0, a, 10)]
#yredcoordinates = 100+100*cos(radians(xval))
ypurplecoordinates = [(400+100*sin(radians(x))) for x in range(0, a, 10)]
#ypurplecoordinates = 400+100*sin(radians(xval))
xpurplecoordinates = [(100+100*cos(radians(x))) for x in range(0, a, 10)]
#xpurplecoordinates = 100+100*cos(radians(xval))

bluee = [Sprite(bluecircle, (x, (100 + 100*sin(radians(x))))) for x in range(0, a, 10) ] 
reed = [Sprite(redcircle, (x, (100+100*cos(radians(x)))))  for x in range(0, a, 10)] 
puurple = [Sprite(purplecircle, ((100+100*cos(radians(x))), (400+100*sin(radians(x))))) for x in range(0, a, 10)]

myapp = App()
myapp.run()