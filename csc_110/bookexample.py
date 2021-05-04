
#bookexample.py
#sumN(n) Returns the sum of the first n natural numbers
#by S. Allen


def sumN(n):
   #start our accumulator
    total = 0
    
    for i in range(n):
        total = total + i

    return total

def main():
    #ask the user for a number
    N = int(input('How many natural numbers do you want to use? '))
    

    #perform sum
    total2 = sumN(N)


    #report the result
    print('The sum of the first',N,'natural numbers is',total2)


main()
    
