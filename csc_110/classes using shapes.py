class Circle:

    def __init__(self, xi, yi, radius):
        self.Radius = radius
        self.x = xi
        self.y = yi


    #getters to access information
    def getRadius(self):
        return self.Radius

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    #geometric calculations
    def area(self):
        return math.pi*self.Radius**2

    def circumference(self):
        return 2*math.pi*self.Radius




class Rectangle:
    def __init__(self, xi, yi, length, width):
        self.Length = length
        self.Width = width
        self.x = xi
        self.y = yi

    #getters
    def getLength(self):
        return self.length

    def getWidth(self):
        return self.width

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    #geometric calculations
    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2*(self.length + self.width)



class Shape:

    def __init__(self, xi, yi):
        self.x = xi
        self.y = yi

    def moveto(self, xnew, ynew):
        self.x = xnew
        self.y = ynew

    #getters
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getcenter(self):
        return (self.x, self.y)
