#create a tictactoe game

#design the board. It needs to have 3 rows, and 3 columns, and so it needs to store
   #9 elements of data.  The elements should be integers for easy recall of each "square"
   # and should be blank to start.  Use a list


board = ["  " for i in range(9)]             #board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

    #make a function to determine which player's turn it is

def player_move(icon):
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2

    print("Your turn player {}".format(number))

    #check to ensure player move doesnt move forward if doubled
    dblchk = False
    while dblchk == False:
        
        choice = int(input("Enter your move (1-9): ").strip())
        if board[choice-1] == "  ":             #applying choice to board should put an X in the numbered
            board[choice -1] = icon                      #board index spot.
            dblchk = True
           
        else:
            print()
            print("That space is taken!")

    #define if someone has won the game

def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

    #define if there is a draw

def is_draw():
    if "  " not in board:
        return True
    else:
        return False

    #pull together how to determine which victory conditions are true

while True:
    print_board()
    player_move("X")
    print_board()
    if is_victory("X"):
        print("X wins! Congrats!")
        break
    elif is_draw():
        print("It's a draw!")
        break
    player_move("O")
    if is_victory("O"):
        print_board()
        print("O wins! Congrats!")
        break
    elif is_draw():
        print("It's a draw!")
        break







            #define how to choose a spot on the board (1 to 9 being board[0] to board[8])

#while True:
    #print_board()
    #choice = int(input("Enter your move (1-9): ").strip())
    #if board[choice-1] == "  ":             #applying choice to board should put an X in the numbered
        #board[choice -1] = "X"                                                     #board index spot.
    #else:
     #   print()
      #  print("That space is taken!")


     
