#from savetime import *
import random


def save_to_file(name_of_file,board):
    f = open(name_of_file,'w')
    f.write(board)
    f.close()



def load_from_file(name_of_file):
    f = open(name_of_file,'w')





def get_board(board):
    lol = ""
    for x in board:
        lol +=  "  ".join(x)  + "\n"

    return lol










def row(board):
    return random.randint(0,len(board) - 1)

def column(board):
    return random.randint(0,len(board[0]) -1)



def main():
    outer_board = []
    game_row = random.randint(0,4)
    game_column = random.randint(0,4)
    for x in range(5):
        outer_board.append(["o"] * 5)
    load = input("Would you like to load a saved game?\n>")
    load = load.upper()
    if load == "YES":
        try:
            file_name = input("What's the name of the file you'd like to load?\n>")
            load_from_file(file_name)
        except:
            print("nice try but that dont exist buddy")



    game_row = row(outer_board)
    game_column = column(outer_board)

    the_question = input("Do you want to input the location of the ship?\nType row,col to set or press ENTER/RETURN to skip\n>")
    question = input("(s)ave, (q)uit or enter a row and column ")

    while question != "q":


        if  question == "s":
            file_name = input("gimme a file name")
            save_to_file(file_name,get_board(outer_board))
        elif "," in question:
            if "," in the_question:
                if question[0] == the_question[0] and question[2] == the_question[2]:
                    ex = int(question[0])
                    why = int(question[2])
                    outer_board[ex][why] = "X"
                    print(get_board(outer_board))
                    print("OMG YOU GOT IT")
                else:
                    ex = int(question[0])
                    why = int(question[2])
                    outer_board[ex][why] = " "
                    print(get_board(outer_board))
                    print("YOU MISSED, YOU SHOULD TRY AGAIN")
            else:
                print(game_row,game_column)
                if question[0] == game_row and question[2] == game_column:
                    ex = int(question[0])
                    why = int(question[2])
                    outer_board[ex][why] = "X"
                    print(get_board(outer_board))
                    print("OMG YOU GOT IT")
                else:
                    ex = int(question[0])
                    why = int(question[2])
                    outer_board[ex][why] = " "
                    print(get_board(outer_board))
                    print("YOU MISSED, YOU SHOULD TRY AGAIN")


        question = input("(s)ave, (q)uit or enter a row and column ")

    print("thank you for playing")
main()















if __name__ == '__main__':
    main()









