#>>> testwin = graphics.GraphWin('Test Window', 200, 200)
#>>> testwin.setCoords(0,0,2,2)
#>>> graphics.Circle(graphics.Point(1,1), 0.5).draw(testwin)
#>>> graphics.Text(graphics.Point(1,1), "Circle!").draw(testwin)


from graphics import *

def main():
    win = GraphWin("Mouse click")
    win.setCoords(-1, -1,1,1)

    p = win.getMouse()

    print('You clicked at',p.getX(),p.getY())

main()
