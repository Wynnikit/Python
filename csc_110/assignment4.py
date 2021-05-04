#assignment4.py
#A program that computes the sum of the squares of numbers read from a file. 
#by S.Allen

def main():
    #open a file, this will be a4test.txt
    fname = input('What is the filename? ')
    infile = open(fname, 'r')
    
    #read it
    a4list = infile.readlines()
            #readlines create a list object that hold the entire file
            #so after 'reading' a file, it can be closed to save resources/cpu cycles

    #close the file
    infile.close()


    #convert the file contents from a string list to a numeric list
    toNumbers(a4list)
      
    #compute the squares for all the values in the file
    squareEach(a4list)

    #sum the squares of the values
    total = sumList(a4list)

    #print the final sum
    print('The sum of the squares of the values in',fname,'is',total)

 
def squareEach(nums):

   for i in range(len(nums)):

       nums[i] = nums[i]**2



def sumList(nums):

    total = 0
    
    for i in range(len(nums)):

        total = total + nums[i]

    return total




def toNumbers(strList):

    for i in range(len(strList)):
    #I want my range to be the length of the list

        strList[i] = float(strList[i])
        # take the str at this index and make it a float



main()
