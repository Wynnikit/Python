
#Write a program that computes the fuel efficiency of a multi-leg journey.
#The program will first prompt for a starting odometer reading and then
#get information about a series of legs.  For each leg, the user enters
#the current odometer reading and the amount of gas used (separated by
#a space).  The user signals the end of the trip with a blank line.
#The program should print out the miles per gallon achieved on each leg
#and the total MPG for the trip.  

#Remember: Your code should be properly formatted according to the standards
#the book has set up and that we have been following in class.
#Your code should also be commented where appropriate.  


def main():
    #- starting odometer
    odostart = float(input('Please enter your starting odometer reading: '))
 
    newodo = odostart

    totalmiles = 0
    totalgas = 0

    numlegs = 0
    mpglist = []
 

    while True:
        
        #for the leg, ask for odometer reading, ask for gals of gas
        leg = input("Please enter the current odometer reading for this leg and amount of gas used in gals (reading gals). (Press <Enter> to exit): ")

         
        if leg != '':

            legmiles, leggas = leg.split()
           
            
            #remember to change to float!
            chmiles = float(legmiles) - newodo

            newodo = float(legmiles)

            totalmiles += chmiles


            chgas = float(leggas)

            totalgas += chgas

            numlegs += 1

            mpglist.append(chmiles/chgas)
            
            




        else:

            for i in range(len(mpglist)) :

                print('Your mpg for leg',i+1,'is', mpglist[i])
            

            print('Your total mpg for this trip is',totalmiles/totalgas)

            break





    #miles will get updated with change in miles, and then the new miles
    #i want miles to be leg's miles
    #each change in 'miles' should be accumulated in the loop
    #totalmiles = totalmiles + chmiles
    #chmiles = miles - 
    #change in miles from start (odostart, and new miles)
    #report each legs change in miles and total change in miles



        #print(float(legmiles), totalmiles)
        #print(newodo, odostart, legmiles)


main()



#break statement for <enter>

#start odometer - current leg = -(change in miles)

#leg(change in miles) / gals for that leg = mpg for leg

#total change in miles / total gals


#print all legs mpg and total mpg for trip 
