#assignment1.py
#A python script that provides the square and the reciprocal of
#a user given value.
# by S. Allen



def squarefunction(myvalue):
    return myvalue**2

def reciprocalfunction(myvalue):
    return 1/myvalue

def testfunction(myvalue):
    
    square = squarefunction(myvalue)
    reciprocal = reciprocalfunction(myvalue)
    print("The square of",myvalue,"is",square)
    print("The reciprocal of",myvalue,"is",reciprocal)

myvalue = eval(input("Please enter a number: "))

testfunction(myvalue)
    
