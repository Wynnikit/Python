#assignment7.py
#A program to find all the primes up to (or including) a number.
#by S. Allen



def main():

#ask for n
    number = int(input('Please enter a whole number: '))
    print()
#create list of range(2, n+1)
    nlist = []

    for i in range(2, number + 1):
        nlist.append(i)

#run sieve against list and get output

    print(sieve(nlist))


    #while/for loop
    #check elements against nlist

        #after x is compared, newlist = list.pop(x)


def sieve(nl): 

    primelist = []

#check elements against multiples until list is empty
    while len(nl) > 0:

        current = nl[0]

        print(current,'is a prime number.\n')

        primelist.append(nl.pop(0))

        for x in nl:  #check if any element in list is a multiple of i

            if x % current == 0: nl.remove(x)
        
  

    return primelist
    


    


main()
