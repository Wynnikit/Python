#assignment1.py
#Write a python script that does the following: 

    #prompts the user for an input value
    #prints the reciprocal value on one line
    #prints the square of value on a second line
    #labels the values with a description of what is being printed.
    #Don't leave any orphan numbers that are unexplained.

# by S. Allen

def main():
    value = eval(input("Please enter a number: "))
    print("The reciprocal of", value, "is",(1 / value))
    print("The square of", value, "is",(value**2))

main()




#Dr. Minter's version:

def squarefunction(myvalue):
    print('The square of',myvalue,'is,'myvalue**2)

def reciprocalfunction(myvalue):
    print('The reciprocal of',myvalue,'is',1/myvalue)

def main(myvalue):  #or testfunction(myvalue)
    squarefunction(myvalue)
    reciprocalfunction(myvalue)

main()
    
