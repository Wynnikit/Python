except  ValueError as excObj :

    if  str(excObj) == "math domain error":

        print("No Real Roots")

    else:

        print("Invalid coefficient given")

except :
    print ("\nSomething went wrong, sorry!")
