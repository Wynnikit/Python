#assignment6.py
#A program that computes the fuel efficiency of a multi-leg journey.
#by S. Allen


def main():
    #- starting odometer
    odostart = float(input('Please enter your starting odometer reading: '))
    print()
    
    newodo = odostart

    totalmiles = 0
    totalgas = 0

    mpglist = []
 

    while True:
        
        #for the leg, ask for odometer reading, ask for gals of gas
        leg = input("Please enter the current odometer reading for this leg and amount of gas used in gals (reading gals). (Press <Enter> to exit): ")
        print()
         
        if leg != '':

            legmiles, leggas = leg.split()
           
            
            #remember to change to float!
            chmiles = float(legmiles) - newodo

            newodo = float(legmiles)

            totalmiles += chmiles


            chgas = float(leggas)

            totalgas += chgas

            mpglist.append(chmiles/chgas)
    

        else:

            for i in range(len(mpglist)) :

                print('Your mpg for leg',i+1,'is', mpglist[i])
            

            print('\nYour total mpg for this trip is {0:0.5}'.format(totalmiles/totalgas))

            break



main()


