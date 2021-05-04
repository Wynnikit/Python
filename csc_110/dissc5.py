#write a program that uses a while loop to determine how long
#it takes for an investment to double at a given interest rate.
#The input will be an annualized interest rate and the output is
#the number of years it takes an investment to double.

#- interest  = principle*rate*time
#- is rate percentage or float?
#- years is time
#- add 1 to the years for each loop
#principal is not imp?
#- balance needs to be doubled
#- need to keep track of balance and principal?
 #  balance= 1, b <2 keep going




def main():
    #time in years
    time = 0

    #starting balance value
    balance = 1

    #  Get interest rate
    rate = float(input("Enter the annualized interest rate as a decimal:  "))

    
    #loop through adding balance and computing interest
    while balance < 2:
        interest = balance * rate * time
        balance = balance + interest
        time += 1

    print('\nIt will take',time,'years for your balance to double.')















main()
