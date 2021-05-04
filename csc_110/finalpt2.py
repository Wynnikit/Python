#finalpt2.py
#Program that creates a face object
#by S. Allen



'''Problem Statement:

We want to write a program that will draw a simple "meh" face.
(Note: it is not a smiley face because the mouth should be a line segment
 rather than an arc).  The face will consist of a head (circle), two eyes
(each circles), a nose (square) and a mouth (line segment).  The user
should be able to set the size of the eyes and the size of the head, the
size of the nose as well as the color of each object but there should be
default values set for each so the user doesn't have to (eyes r=10,
head r=50,nose width = 10).  The distance between the objects should be fixed.

We want our faces to be objects so we will define a new class called Face.
Using the graphics.py library, write a program that defines the Face class
and then demonstrates how to use it by drawing two faces to a window. Your
script should contain a class definition as well as a function that uses the
class.  

Remember points here are for demonstrating an understanding of the concepts.
Do you know how to define a class.  Do you know what goes into a class?
There are a few points for fully functional code but vast majority of points
are for demonstrating good design principles (example: abstraction,
encapsulation and polymorphism).  If you are worried about time, think about
our design principles and demonstrate the concepts.  '''


from graphics import *
import math

# Tried to do seperate classes for each object for relational positioning.
# It didn't work well


class Head(Circle):
    def __init__(self, center=Point(-100,100), radius=80):
        Circle.__init__(self, center, radius)
        self.center = center
        self.radius = radius
        self.setFill("white")
    
    
    #def getColor(color):
        #return self.color

class Nose(Rectangle):
    def __init__(self, center=Point(-100,100)):
        self.center = center
        
        p1 = Point((center.getX()-5),(center.getY()-5))
        p2 = Point((center.getX()+5),(center.getY()+5))
        Rectangle.__init__(self, p1, p2)
        
        self.setFill("red")

class Eyes(Circle):
    def __init__(self, center=Point(0,0), radius=15):
        #center=Point((Head.self.getCenter().getX()-20), (Head.self.getCenter().getY()+20)), radius=10):
        #Head.__init__(self, center=Point(-100,100), radius=80)
        Circle.__init__(self, center, radius)
        self.center = center
        self.radius = radius
        self.setFill("blue")

        

class Mouth(Line):
    def __init__(self, center=Point(0,0)):
        self.center = center
        p1 = Point((center.getX()-30),(center.getY()-30))
        p2 = Point((center.getX()+30),(center.getY()-30))

        Line.__init__(self, p1, p2)
    
### No idea how to pass in user parameters without possible for loop/list
        
class Face: #(GraphicsObject):?
    #def __init__(self, options=["outline", "fill", "justify"], center=Point(0,0), radius=100):

    def __init__(self, 
        self.center = center
        self.head = Head()
        self.nose = Nose()
        self.eye = Eyes()
        self.mouth = Mouth()
        self.radius = radius

        #GraphicsObject.__init__(self, options)

    def setHead(self, hsize, hcolor):
        head = Head(Point(100,-100), hsize/2)
        head.setFill(hcolor)
        center = head.getCenter()

    def setNose(self, nsize, ncolor):
        nose = Nose(center)

        eye1 = Eyes(Point((center.getX()-30),(30+center.getY())))
        eye2 = eye1.clone()
        eye2.move(60,0)

        mouth = Mouth(center)
        mouth.draw(win)





### test runs fine, when you comment out the face class above
    #but again, not user input.
        
def test():
    win = GraphWin("Let's Make a Face!", 500, 500)
    win.setCoords(-250,-250,250,250)

    #width = 

    #face = Face()
    #face.draw(win)
    head = Head()

    head.setFill("cyan")

    head.draw(win)
    
    center = head.getCenter()
    nose = Nose(center)
    nose.draw(win)

    eye1 = Eyes(Point((center.getX()-30),(30+center.getY())))
    eye2 = eye1.clone()
    eye2.move(60,0)
    eye1.draw(win)
    eye2.draw(win)

    mouth = Mouth(center)
    mouth.draw(win)

test()
    

def main():
    
    #make window
    win = GraphWin("Let's Make a Face!", 500, 500)
    win.setCoords(-250,-250,250,250)

    #draw the default face at point(-100,100)
    defface = Face()
    defface.draw(win)
    

    #user generated face at (100,-100)
    #faceparams = []?

    hsize = int(input("Size of head, (ex. 50), Press <Enter> for default: "))
    #faceparams.append(hsize/2) #radius
    
    
    hcolor = input('What color should the head be?: ')
    #head.setFill = hcolor

    esize = int(input("How big would you like the eyes to be?(ex. 20): "))
    #eye.radius = esize/2
    
    
    ecolor = input('What color should the eyes be?: ')

    nsize = int(input("How big would you like the nose to be?(ex. 20): "))
    ncolor = input('What color should the nose be?: ')

    face = Face()


    face.draw(win)











#main()
