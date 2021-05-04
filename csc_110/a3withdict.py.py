
# a3withdict.py
# A program that reads a file of student data,
# prints the data, and saves it to a new file.
#Now with a dictionary!
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

 


#number of scores appended to list?
    #len(scorelist)
    
    #how to sum values in a list?
    #totalscores += score   
    #scorelist.append(score)

    
#declare dict

    
    students= {}

#loop over data in file
    for line in infile:

        first, last, score =  line.split()

        students[first+' '+last] = int(score)

    


#compute the avg
    totalavg = sum(students.values())/len(students.values())


#loop over data to compare avg
    for i in students:
        
         
        if students[i] <60: letterscore = 'F'
        elif 60 <= students[i] <70: letterscore = 'D'
        elif 70 <= students[i] <80: letterscore = 'C'
        elif 80 <= students[i] <90: letterscore = 'B'
        else: letterscore = 'A'



        if students[i] < totalavg:
            diff = totalavg - students[i]
            print('{0} {1} scored {2} points below average for a grade of {3}.'.format(i, students[i],diff,letterscore))
        
        elif students[i] > totalavg:
            diff = students[i] - totalavg
            print('{0} {1} scored {2} points above avereage for a grade of {3}.'.format(i, students[i],diff,letterscore))

        else:
            print('{0} {1} recieved the average score of {2} for a grade of {3}.'.format(i, students[i],currentscore,letterscore))




        newdata = print(i, students[i], letterscore, file=outfile)
        #saves the new variable to a different file.



  
#close file

    infile.close()

    outfile.close()


main()
