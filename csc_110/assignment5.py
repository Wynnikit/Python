#assignment5.py
#This program converts numerical credits to a school class type.
#by S. Allen

def main():

    try:
        Ncredits = eval(input("Please enter the number of credits earned: "))

        #Make sure no value is less than zero. (Not sure how to make it an error)
        if Ncredits < 0:

            print("\nPlease use only positive numbers!")

        else:
            
            print("\nYou are a",Level(Ncredits)+ '.')


    #If user inputs a word number ('three' vs. 3):
    except NameError as e:

        print("\nPlease enter a numeral not a word!")

    except:

        print ("\nSomething went wrong, sorry!")

  #Lookup table for credits
def Level(creds):
    
        
        if creds <7 : classlevel = "Freshman"

        elif 7<= creds <16: classlevel = "Sophomore"

        elif 16<= creds <26: classlevel = "Junior"

        else: classlevel = "Senior"

        return classlevel


main()



