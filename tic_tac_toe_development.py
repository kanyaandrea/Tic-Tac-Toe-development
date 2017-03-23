import os
import random
import time


def ask_player_name():
    os.system('clear')
    player1_name = input("Please enter the first player's name:  ")
    os.system('clear')
    player2_name = input("Please enter the second player's name:  ")
    return player1_name, player2_name


def welcome_screen():
    print("\n\n\n")
    print("    ╦ ╦┌─┐┬  ┌─┐┌─┐┌┬┐┌─┐    ")
    print("    ║║║├┤ │  │  │ ││││├┤     ")
    print("    ╚╩╝└─┘┴─┘└─┘└─┘┴ ┴└─┘    ")
    print("          ┌┬┐┌─┐             ")
    print("           │ │ │             ")
    print("           ┴ └─┘             ")
    print("╔╦╗┬┌─┐  ╔╦╗┌─┐┌─┐  ╔╦╗┌─┐┌─┐")
    print(" ║ ││     ║ ├─┤│     ║ │ │├┤ ")
    print(" ╩ ┴└─┘   ╩ ┴ ┴└─┘   ╩ └─┘└─┘")
    print("        ╔═╗╔═╗╔╦╗╔═╗         ")
    print("        ║ ╦╠═╣║║║║╣          ")
    print("        ╚═╝╩ ╩╩ ╩╚═╝         ")
    print("\n\n\n")
    time.sleep(2)


def player_input():
    os.system("clear")
    marker = ""
    while not (marker == "X" or marker == "O"):
        marker = input(player_names[0] + " do you want to be X or O?  ").upper()

    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")


def display_board(board):
    os.system('clear')  # Ezzel a paranccsal tudjuk torolni a kepernyot.
    print("\n"*2)
    print(("    |     |    ").center(50, " "))
    print((" " + board[7] + "  |  " + board[8] + "  |  " + board[9] + " ").center(50, " "))
    print(("    |     |    ").center(50, " "))
    print(("-----------------").center(50, " "))
    print(("    |     |    ").center(50, " "))
    print((" " + board[4] + "  |  " + board[5] + "  |  " + board[6] + " ").center(50, " "))
    print(("    |     |    ").center(50, " "))
    print(("-----------------").center(50, " "))
    print(("    |     |    ").center(50, " "))
    print((" " + board[1] + "  |  " + board[2] + "  |  " + board[3] + " ").center(50, " "))
    print(("    |     |    ").center(50, " "))
    print("\n"*2)


def place_marker(board, position, marker):
    board[position] = marker


def win_check(board, mark):
    if board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    elif board[3] == mark and board[5] == mark and board[7] == mark:
        return True
    else:
        return False


def choose_first():
    os.system("clear")
    if random.randint(0, 1) == 0:
        print(("\n" * 9 + player_names[0] + " starts the game now!!!").upper())
        time.sleep(2)
        return player_names[0]
    else:
        print(("\n" * 9 + player_names[1] + " starts the game now!!!").upper())
        time.sleep(2)
        return player_names[1]


def space_check(board, position):
    if board[position] == " ":
        return True
    else:
        return False


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = ""
    while position not in "1 2 3 4 5 6 7 8 9".split() or not space_check(board, int(position)):
        position = input("Please enter your mark's position: (1-9)  ")
    return int(position)


def replay():
    return ("Do you want to play again? Y/N  ".upper().startswith("Y"))


def main():
    turn = choose_first()  # Ez a valtozo egy string amely a kezdo jatekos nevet tartalmazza.
    game_on = True
    the_board = [" "] * 10

    while game_on is True:

        if turn == player_names[0]:  # A lista 0. eleme az elso jatekos nevet tartalmazza.
            display_board(the_board)
            print(player_names[0], ":")
            position = player_choice(the_board)
            place_marker(the_board, position, player_marker_choice[0])

            if win_check(the_board, player_marker_choice[0]) is True:
                display_board(the_board)
                print("Congratulation " + player_names[0] + "!!! You won the game!")
                game_on = False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("This game is draw!")
                    break
                else:
                    turn = player_names[1]

        else:
            turn = player_names[1]
            display_board(the_board)
            print(player_names[1], ":")
            position = player_choice(the_board)
            place_marker(the_board, position, player_marker_choice[1])

            if win_check(the_board, player_marker_choice[1]) is True:
                display_board(the_board)
                print("Congratulation " + player_names[1] + "!!! You won the game!")
                game_on = False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("This game is draw!")
                    break

                else:
                    turn = player_names[0]


new_game = "y"
while new_game == "y":
    welcome_screen()
    player_names = ask_player_name()  # Ez a valtozo egy lista ami mindket jatekos nevet tartalmazza.
    player_marker_choice = player_input()  # Ez a valtozo 1 ket elemes tuple, ami tartalmazza a jatekosok markeret.
    main()
    new_game = input("Do you want to play a new game? (write y to continue, or press any key to exit)" )
exit()