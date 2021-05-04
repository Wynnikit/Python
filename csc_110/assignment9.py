#assignment9.py
#Program that finds intercept points between a circle and a line if they exist.
#by S. Allen


'''Write an interactive graphics program that finds the intersection(s)
of a circle and horizontal line.

Interactive Input:  

    A mouse click to determine the radius of the circle
    a text entry (in graphics window) to determine the y-intercept
    of the line segment

Output:

    Draw a circle centered at (0,0) with given radius in a window with
    coordinates such that x runs from -10 to 10 and y runs from -10 to 10.  
    In the same window, draw a horizontal line segment with the specified
    y-intercept. In the same window, draw any intersection point(s) in red
    Print out the coordinates of the intersection(s) if any.  (Note it says
                                                               print not draw)

Formula: (see book)Formula: x = ± sqrt(r**2-y**2)

Note: This problem is based on a textbook exercise but asks for the
    information in a very different way.  



need a window 10x10
start circle creation, in parameters, getmouse input for radius
    r = radius'''


from graphics import *
import math


def main():
    #make a window
    win = GraphWin("Circle Intercept Points", 400, 400)

    win.setCoords(-10, -10, 10, 10)

    center = Point(0,0)
    center.draw(win)

    click = Text(Point(0,3),'Click anywhere to set a radius')
    click.draw(win)

    #point for radius
    crad = win.getMouse()

    #length calc or radius
    dx = crad.getX()
    dy = crad.getY()

    radius = math.sqrt( dx**2 + dy**2)

    #remove text
    click.undraw()
    
    #make the circle
    circle = Circle(center, radius)
    circle.draw(win)
    
    #make text box for y int
    text = Text(Point(-8, 9.25), "Enter y-int:")
    text.draw(win)
    input = Entry(Point(-5.3, 9.25), 3)
    input.draw(win)

    button = Text(Point(-3.6, 9.25),"Go!")
    button.draw(win)
    Rectangle(Point(-4.4,8.7), Point(-2.8, 9.9)).draw(win)

    #Wait for mouse click
    win.getMouse()
    

    yint = float(input.getText())

    #make line
    line = Line(Point(-9.5, yint), Point(9.5,yint))
    line.draw(win)

    #overlap??
    try:
        x1 = math.sqrt(radius**2-yint**2)
        x2 = float(-x1)

    except ValueError:
        print('This line does not intersect the circle.')

        #wait for click and then quit
        click2 = Text(Point(0,3),'Click to end')
        click2.draw(win)

        win.getMouse()
        win.close()
        return   #exits function main?

    #if overlap exists
    xover1 = Point(x1,yint)
    xover2 = Point(x2,yint)

    xover1.setFill('red')
    xover2.setFill('red')

    xover1.draw(win)
    xover2.draw(win)


#print results
    if x1 == 0:
        print('The intercept point is ({0:0.3}, {1:0.3}).'.format(xover1.getX(), xover1.getY()))

    else:
        print('The intercept points are ({0:0.3}, {1:0.3}) and ({2:0.3}, {3:0.3}).'.format(xover1.getX(), xover1.getY(),xover2.getX(), xover2.getY()))   


    #wait for click and then quit
    click2 = Text(Point(0,2),'Click to end')
    click2.draw(win)

    win.getMouse()
    win.close()



main()

    
    
                    
