import random


def bot_check_for_defense(combinations, board):
    slot_options = []
    runs = 0
    for combination in combinations:
        if board[combination[0]][combination[1]] == 1 and board[combination[2]][combination[3]] == 1 and board[combination[4]][combination[5]] == 0:
            # left and middle set by player
            # print("slot 3")
            runs += 1
            slot_options.append([combination[4], combination[5]])
        elif board[combination[2]][combination[3]] == 1 and board[combination[4]][combination[5]] == 1 and board[combination[0]][combination[1]] == 0:
            # print("slot 1")
            runs += 1
            slot_options.append([combination[0], combination[2]])
            # middle and left set by player
        elif board[combination[0]][combination[1]] == 1 and board[combination[4]][combination[5]] == 1 and board[combination[2]][combination[3]] == 0:
            # print("slot 2")
            runs += 1
            slot_options.append([combination[2], combination[3]])
        else:
            runs += 1
    print(slot_options)
    result = [board, slot_options]
    return result


def bot_check_duplicate_defence_position(defence_slot_options):
    completions = [1, 2]
    for _ in completions:
        if len(defence_slot_options) == 0:
            #print("0  possibilities")
            break
        elif len(defence_slot_options) == 1:
            #print("only one possibility"
            break
        elif len(defence_slot_options) > 1:
            #print("printing length of defence_slot_options:")
            #print(len(defence_slot_options))
            #print()
            for option in range(len(defence_slot_options)):
                #print("selected option number: ", option)
                for check_option in range(len(defence_slot_options)):
                    #print("selected checking number: ", check_option)
                    if option != check_option:
                        #print("option(index) is not equal to check_option")
                        #print()
                        if defence_slot_options[option] == defence_slot_options[check_option]:
                            #print()
                            #print("option and check_option contain the same data inside defence_slot_options:")
                            #print("      option: ", option)
                            #print("          inside defence_slot_options: ", defence_slot_options[option])
                            #print("      check_option: ", check_option)
                            #print("          inside defence_slot_options: ", defence_slot_options[check_option])
                            #print()
                            #print("last if statement: ", defence_slot_options[check_option], check_option)
                            defence_slot_options.remove(defence_slot_options[int(check_option)])
                            print(defence_slot_options)
                            break
                else:
                    continue
                break
    return defence_slot_options


def read_ttt_board(ttt_board_raw, char1, char2):
    ttt_board_result = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    times = -1
    for row in ttt_board_raw:
        for col in row:
            times += 1
            if col == 1:
                ttt_board_result[times] = char1
            if col == 0:
                ttt_board_result[times] = " "
            if col == 2:
                ttt_board_result[times] = char2
    return ttt_board_result


def print_board(board_result):
    print(" [" + board_result[0] + "] [" + board_result[1] + "] [" + board_result[2] + "] ")
    print(" [" + board_result[3] + "] [" + board_result[4] + "] [" + board_result[5] + "] ")
    print(" [" + board_result[6] + "] [" + board_result[7] + "] [" + board_result[8] + "] ")


character1 = "X"
character2 = "O"

ttt_board = [
    [1, 1, 1],
    [1, 1, 1],
    [0, 1, 1]
]

win_combinations = [
    [0, 0, 0, 1, 0, 2],
#    0  1  2  3  4  5
    [1, 0, 1, 1, 1, 2],
    [2, 0, 2, 1, 2, 2],
    [0, 0, 1, 0, 2, 0],
    [0, 1, 1, 1, 2, 1],
    [0, 2, 1, 2, 2, 2],
    [0, 0, 1, 1, 2, 2],
    [0, 2, 1, 1, 2, 0]
]

bot_check_for_defense_result = bot_check_for_defense(win_combinations, ttt_board)
ttt_board = bot_check_for_defense_result[0]
bot_defence_slot_options = list(bot_check_for_defense_result[1])
bot_defence_slot_options = bot_check_duplicate_defence_position(bot_defence_slot_options)
bot_defence_slot_options = bot_check_duplicate_defence_position(bot_defence_slot_options)
bot_defence_slot_options = bot_check_duplicate_defence_position(bot_defence_slot_options)
ttt_board_result = read_ttt_board(ttt_board, character1, character2)
print_board(ttt_board_result)
print(bot_defence_slot_options)


list = [1, 2, 4, 3, 6, 7]
#       0  1  2  3  4  5