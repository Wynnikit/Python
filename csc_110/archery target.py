#archery target.py
#create archery target using circle class
#by S.Allen



import graphics

def main():

    #archwin = graphics.GraphWin("Archery Target", 400, 400)

    center = graphics.Point(201, 201)
    radius = 380/10

    #whring = graphics.Circle(center, 5*radius)
    #whring.draw(archwin)

    #blackring = graphics.Circle(center, 4*radius)
    #blackring.setFill("black")
    #blackring.draw(archwin)

    #bluering = graphics.Circle(center, 3*radius)
    #bluering.setFill("blue")
    #bluering.draw(archwin)

    #rring = graphics.Circle(center, 2*radius)
    #rring.setFill("red")
    #rring.draw(archwin)
    
    #bullseye = graphics.Circle(center, radius)
    #bullseye.setFill("yellow")
    #bullseye.draw(archwin)


#assume user wants a squarse window"
    width = input("How big do you want your window?: ")
    archwin = graphics.GraphWin("Archery Target", width, width)

    colors = ["none","yellow","red","blue","black","white"]
    circles = []

    for i in range(5,0, -1):
        circ = graphics.Circle(center, i*radius)
        circ.setFill(colors[i])
        circ.draw(archwin)
        
        circles.append(circ)

main()

