

ttt_board_shown = ["1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]

print(" [" + ttt_board_shown[0] + "] [" + ttt_board_shown[1] + "] [" + ttt_board_shown[2] + "] ")
print(" [" + ttt_board_shown[3] + "] [" + ttt_board_shown[4] + "] [" + ttt_board_shown[5] + "] ")
print(" [" + ttt_board_shown[6] + "] [" + ttt_board_shown[7] + "] [" + ttt_board_shown[8] + "] ")

ttt_board = [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]

print("")


def player_set_newposition(ttt_board):
    player_new_position = int(input("Bitte gib ein wo du dein erstes Kreuz setzen willst: ")) - 1
    if ttt_board[player_new_position] == " ":
        ttt_board[player_new_position] = "X"
    else:
        print("Incorrect number. Please try again.")
        print("")


    return ttt_board

print(player_set_newposition(ttt_board))

print(" [" + ttt_board[0] + "] [" + ttt_board[1] + "] [" + ttt_board[2] + "] ")
print(" [" + ttt_board[3] + "] [" + ttt_board[4] + "] [" + ttt_board[5] + "] ")
print(" [" + ttt_board[6] + "] [" + ttt_board[7] + "] [" + ttt_board[8] + "] ")

print(ttt_board)


print(player_set_newposition(ttt_board))

if ttt_board[0] == "X" and ttt_board[1] == "X":
    ttt_board[2] = "O"
elif ttt_board[0] == "X" and ttt_board[4] == "X":
    ttt_board[8] = "O"
elif ttt_board[1] == "X" and ttt_board[2] == "X":
    ttt_board[0] = "O"
elif ttt_board[2] == "X" and ttt_board[4] == "X":
    ttt_board[6] = "O"
elif ttt_board[3] == "X" and ttt_board[4] == "X":
    ttt_board[5] = "O"
elif ttt_board[4] == "X" and ttt_board[5] == "X":
    ttt_board[3] = "O"
elif ttt_board[6] == "X" and ttt_board[7] == "X":
    ttt_board[8] = "O"
elif ttt_board[7] == "X" and ttt_board[8] == "X":
    ttt_board[6] = "O"
elif ttt_board[0] == "X" and ttt_board[3] == "X":
    ttt_board[6] = "O"
elif ttt_board[1] == "X" and ttt_board[5] == "X":
    ttt_board[7] = "O"
elif ttt_board[2] == "X" and ttt_board[5] == "X":
    ttt_board[8] = "O"
elif ttt_board[6] == "X" and ttt_board[3] == "X":
    ttt_board[0] = "O"
elif ttt_board[6] == "X" and ttt_board[7] == "X":
    ttt_board[8] = "O"

combinations = [[0, 1, 2], [3, 4, 5 ], [6, 7, 8]]
print(combinations[1])


#kann mehrere möglichkeiten gleichzeitig haben und das kann dazu führen das auf dauer sich sachen immer widerholen



print(" [" + ttt_board[0] + "] [" + ttt_board[1] + "] [" + ttt_board[2] + "] ")
print(" [" + ttt_board[3] + "] [" + ttt_board[4] + "] [" + ttt_board[5] + "] ")
print(" [" + ttt_board[6] + "] [" + ttt_board[7] + "] [" + ttt_board[8] + "] ")

print(ttt_board)