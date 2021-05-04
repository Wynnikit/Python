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

        
    choice = int(input("Enter your move (1-9): ").strip())
    if board[choice-1] == "  ":             #applying choice to board should put an X in the numbered
        board[choice -1] = icon                      #board index spot.
        return True
           
    else:
        print()
        print("That space is taken!")
        return False

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


playerturn = "X"
print_board()

while True:
    if player_move(playerturn):

        if is_victory(playerturn):
            print(" {} Wins".format(playerturn))
            break

        if is_draw():
            print("It is a Draw")
            break

        if playerturn == "X":
            playerturn = "O"
        else:
            playerturn = "X"

        print_board()
