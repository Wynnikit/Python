
#cubed book ex.py
#sumNCubes(n) Returns the sum of the cubes first n natural numbers and
#sumN(n) returns the sum of the first n natural numbers
#by S. Allen


def sumNCubes(n):
   #start our accumulator
    total = 0
    
    for i in range(n):
        total = total + i**3

    return total

def sumN(n):
   #start our accumulator
    total1 = 0
    
    for i in range(n):
        total1 = total1 + i

    return total1



def main():
    #ask the user for a number
    N = int(input('How many natural numbers do you want to use? '))
    

    #perform sum
    totalcube = sumNCubes(N)
    totalsum = sumN(N)

    #report the results
    print('The sum of the first',N,'natural numbers is',totalsum)
    print('The sum of the cubes of the first',N,'natural numbers is',totalcube)


main()
    
