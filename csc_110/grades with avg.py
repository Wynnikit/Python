
# grades with avg.py
# A program that reads a file of student data,
# prints the data, and saves it to a new file.
#Now with lists!
#by S. Allen



def main():

    print('This program will show you the grades of each student in')
    print('a file and saves them to grades.dat','\n')

    #get the info on the file          
    fname = input('What is the filename? ')
        # this will be scores.dat

    print()

    infile = open(fname, 'r')
    outfile = open('grades.dat', 'w')
        # welcome.dat is where the output will be saved


#start accumulator for avg

    totalscores = 0


#number of scores appended to list?
    #len(scorelist)
    
    #how to sum values in a list?
    #totalscores += score   
    #scorelist.append(score)

    
#declare empty lists
    scorelist = []
    firstlist = []
    lastlist = []

    


#loop over data in file
    for line in infile:

        first, last, score =  line.split()

        firstlist.append(first)
        lastlist.append(last)
        scorelist.append(score)

        totalscores += int(score)
    


#compute the avg
    totalavg = totalscores /len(scorelist)



#loop over data to compare avg
    for i in range(len(scorelist)):

        currentscore = int(scorelist[i])
         
        if currentscore <60: letterscore = 'F'
        elif 60 <= currentscore <70: letterscore = 'D'
        elif 70 <= currentscore <80: letterscore = 'C'
        elif 80 <= currentscore <90: letterscore = 'B'
        else: letterscore = 'A'



        if currentscore < totalavg:
            diff = totalavg - currentscore
            print('{0} {1} scored {2} points below average for a grade of {3}.'.format(firstlist[i],lastlist[i],diff,letterscore))
        
        elif currentscore > totalavg:
            diff = currentscore - totalavg
            print('{0} {1} scored {2} points above avereage for a grade of {3}.'.format(firstlist[i],lastlist[i],diff,letterscore))

        else:
            print('{0} {1} recieved the average score of {2} for a grade of {3}.'.format(firstlist[i],lastlist[i],currentscore,letterscore))




        newdata = print(firstlist[i], lastlist[i], currentscore, letterscore, file=outfile)
        #saves the new variable to a different file.



  
#close file

    infile.close()

    outfile.close()


main()
