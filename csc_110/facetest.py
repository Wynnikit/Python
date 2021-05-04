from graphics import *
import math


'''class Face(GraphicsObject):

    def __init__(self):
        self.head = "head"
        self.eye = "eye"
        self.nose = "nose"
        self.mouth = "mouth"

    
   #head -circle
    def makeHead(self, size=Circle(center=Point(200,200), radius=20), color="beige"):
        size = Circle(center=Point(200,200), radius=20)  
        #self.setFill(color)

    def getHead(self):
        return self.head

class Face(graphics._BBox):

    def __init__(self):
        


        _BBox.__init__(self, p1, p2)
        #head = Circle(xi=200, yi=200, radius=20)

        



        #eye2 = self.eye.clone()'''



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
    

#class Face(GraphicsObject):
    #def __init__(self, [Head(), Nose(), Eyes(), Mouth(), center=Point(0,0),):
        #self.center = center
        #self.head = Head()
        #self.nose = Nose()
        #self.eye = Eyes()
        #self.mouth = Mouth()
        #self.radius = radius
        

def main():
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



main()
