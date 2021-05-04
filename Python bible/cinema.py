#create films dictionary

films= {
    "Finding Dory": [3, 5],
    "Bourne": [18, 5],
    "Tarzan": [15, 2],
    "Ghost Busters": [12, 5]
    }

#ask user which film and check if the user is of age

while True:

    choice = input("Which film would you like to watch?: ").strip().title()

    if choice in films:
        age = int(input("How old are you?: ").strip())

        #check user age

        if age >= films[choice][0]:
            # check if enough seats

            num_seats = films[choice][1]

            if num_seats > 0:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1] - 1
            else:
                print("Sorry! We are sold out!")
                
        else:
            print("You are too young for this film.")

            
    else:
        print("We don't have that film...")
