








def main():
    print('This program calculates the mean and median of an odd numbered series.')
    print()
    print()
    
    digits = eval(input('How many numbers are in this set? '))
    #storing the quantity of numbers for later
    
    print()
    print()
    

    # to find median, take amt of numbers, subt 1, div by 2
    # this = index position of median
    
    
    total = 0
    #sum total of all the numbers inputted.


    #take ((digits // 2) + 1) = median target marker


    
    for loop in range(digits // 2):

        x = eval(input('Please enter a number: '))

        total = total + x



    for i in range(1):

        y = eval(input('Please enter a number: '))

        median = y

        total = total + y

    
    for loop in range(digits // 2):

        x = eval(input('Please enter a number: '))

        total = total + x

    mean = total / digits
    #to find the mean add all input numbers / digits

    print()
    print()
    
    print('The mean of these numbers is ',mean)
    print()
    print()
    print('The median of these numbers is ',median)


main()
