
# Student grades.py
# A program that reads a file of student data,
# prints the data, and saves it to a new file.
#by S. Allen

def main():

    print('This program will show you the grades of each student in')
    print('a file and saves them to grades.dat','\n')

              
    fname = input('What is the filename? ')
        # this will be scores.dat

    print()

    infile = open(fname, 'r')
    outfile = open('grades.dat', 'w')
        # welcome.dat is where the output will be saved

    for line in infile:

        first, last, score =  line.split() #bc lists don't like integers and python sucks.

##      #score = eval(score)
        #bc python thinks strings cant be compared the way I think.
        
#NEW, Trial 1:     (doesn't need gradescale list)
    
        if int(score) <60: letterscore = 'F'
        elif 60 <= int(score) <70: letterscore = 'D'
        elif 70 <= int(score) <80: letterscore = 'C'
        elif 80 <= int(score) <90: letterscore = 'B'
        else: letterscore = 'A'



        print('{0} {1} recieved a score of {2} for a grade of {3}.'.format(first,last,score,letterscore))
        #prints to screen ^

        newdata = print(first, last, score, letterscore, file=outfile)
        #saves the new variable to a different file.







  


    infile.close()

    outfile.close()


main()



 
