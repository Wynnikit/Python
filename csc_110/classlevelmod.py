# class level assignment script, classlevelmod.py
#CSC 110 Week 5, Lecture 1
#by S. Allen
    

def Level():
    classlevel = "None"

    Ncredits = eval(input("Please enter the number of credits earned: "))

    if Ncredits<45: classlevel = "Freshman"

    elif 45<= Ncredits <90: classlevel = "Sophomore"

    elif 90<= Ncredits <135: classlevel = "Junior"

    else: classlevel = "Senior"


    
    print("Student is a",classlevel)

Level()
