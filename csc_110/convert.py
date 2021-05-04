#convert.py
# A program to convert between inches and feet
# by S. Allen

def main():
    inches = eval(input("How long is your object in inches? "))
    feet = inches * (1/12)
    print("Your object is", feet, "feet long.")

main()
