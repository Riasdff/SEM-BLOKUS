import tkinter as tk
from tkinter import ttk
from tkinter import *
from progression import *
import random
from copy import deepcopy

piece_numbers_ai_y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
piece_numbers_ai_g = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
pieces = [[(0, 0)],
          [(0, 0), [1, 0]],
          [(0, 0), [-1, 0], [1, 0]],
          [(0, 0), [0, -1], [1, 0]],
          [(0, 0), [-1, 0], [1, 0], [2, 0]],
          [(0, 0), [0, -1], [0, 1], [1, 1]],
          [(0, 0), [1, 0], [1, -1], [0, -1]],
          [(0, 0), [0, -1], [1, 1], [1, 0]],
          [(0, 0), [0, 1], [1, 0], [-1, 0]],
          [(0, 0), [-1, 0], [0, -1], [1, -1], [0, 1]],
          [(0, 0), [-1, 0], [-2, 0], [1, 0], [2, 0]],
          [(0, 0), [0, 1], [0, -1], [0, -2], [1, 1]],
          [(0, 0), [0, -1], [0, 1], [1, -1], [1, -2]],
          [(0, 0), [0, 1], [0, -1], [1, -1], [1, 0]],
          [(0, 0), [0, 1], [0, -1], [-1, -1], [1, -1]],
          [(0, 0), [-1, 0], [-1, -1], [1, 0], [1, -1]],
          [(0, 0), [-1, 0], [-2, 0], [0, -1], [0, -2]],
          [(0, 0), [0, 1], [-1, 1], [1, -1], [1, 0]],
          [(0, 0), [-1, 0], [0, -1], [1, 0], [0, 1]],
          [(0, 0), [-1, -1], [0, -1], [0, 1], [0, -2]],
          [(0, 0), [0, -1], [-1, -1], [1, 1], [0, 1]]
          ]
rotate_counter = 0
piece_rotations = [[[(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)]],
                   [[(0, 0), [1, 0]], [(0, 0), [0, -1]], [(0, 0), [-1, 0]], [(0, 0), [0, 1]]],
                   [[(0, 0), [-1, 0], [1, 0]], [(0, 0), [0, 1], [0, -1]], [(0, 0), [1, 0], [-1, 0]], [(0, 0), [0, -1], [0, 1]]],
                   [[(0, 0), [0, -1], [1, 0]], [(0, 0), [-1, 0], [0, -1]], [(0, 0), [0, 1], [-1, 0]], [(0, 0), [1, 0], [0, 1]]],
                   [[(0, 0), [-1, 0], [1, 0], [2, 0]], [(0, 0), [0, 1], [0, -1], [0, -2]], [(0, 0), [-1, 0], [1, 0], [-2, 0]], [(0, 0), [0, -1], [0, 1], [0, 2]]],
                   [[(0, 0), [0, -1], [0, 1], [1, 1]], [(0, 0), [1, 0], [-1, 0], [1, -1]], [(0, 0), [0, -1], [-1, -1], [0, 1]], [(0, 0), [-1, 0], [-1, 1], [1, 0]]],
                   [[(0, 0), [1, 0], [1, -1], [0, -1]], [(0, 0), [-1, 0], [-1, -1], [0, -1]], [(0, 0), [-1, 1], [-1, 0], [0, 1]], [(0, 0), [0, 1], [1, 0], [1, 1]]],
                   [[(0, 0), [0, -1], [1, 1], [1, 0]], [(0, 0), [-1, 0], [0, -1], [1, -1]], [(0, 0), [0, -1], [1, 1], [1, 0]], [(0, 0), [-1, 0], [0, -1], [1, -1]]],
                   [[(0, 0), [0, 1], [1, 0], [-1, 0]], [(0, 0), [1, 0], [0, 1], [0, -1]], [(0, 0), [0, -1], [1, 0], [-1, 0]], [(0, 0), [-1, 0], [0, 1], [0, -1]]],
                   [[(0, 0), [-1, 0], [0, -1], [1, -1], [0, 1]], [(0, 0), [-1, 0], [-1, -1], [1, 0], [0, 1]], [(0, 0), [-1, 1], [0, -1], [0, 1], [1, 0]], [(0, 0), [1, 0], [-1, 0], [1, 1], [0, -1]]],
                   [[(0, 0), [-1, 0], [-2, 0], [1, 0], [2, 0]], [(0, 0), [0, -1], [0, -2], [0, 1], [0, 2]], [(0, 0), [-1, 0], [-2, 0], [1, 0], [2, 0]], [(0, 0), [0, -1], [0, -2], [0, 1], [0, 2]]],
                   [[(0, 0), [0, 1], [0, -1], [0, -2], [1, 1]], [(0, 0), [-1, 0], [-2, 0], [1, 0], [1, -1]], [(0, 0), [-1,-1], [0, -1], [0, 1], [0, 2]], [(0, 0), [-1, 1], [-1, 0], [1, 0], [2, 0]]],
                   [[(0, 0), [0, -1], [0, 1], [1, -1], [1, -2]], [(0, 0), [-1, -1], [-2, -1], [-1, 0], [1, 0]], [(0, 0), [-1, 1], [-1, 2], [0, 1], [0, -1]], [(0, 0), [-1, 0], [1, 0], [1, 1], [2, 1]]],
                   [[(0, 0), [0, 1], [0, -1], [1, -1], [1, 0]], [(0, 0), [1, 0], [0, -1], [-1, -1], [-1, 0]], [(0, 0), [0, -1], [0, 1], [-1, 1], [-1, 0]], [(0, 0), [-1, 0], [1, 0], [0, 1], [1, 1]]],
                   [[(0, 0), [0, 1], [0, -1], [-1, -1], [1, -1]], [(0, 0), [1, 0], [-1, 0], [-1, -1], [-1, 1]], [(0, 0), [-1, 1], [0, -1], [1, 1], [0, 1]], [(0, 0), [-1, 0], [1, -1], [1, 1], [1, 0]]],
                   [[(0, 0), [-1, 0], [-1, -1], [1, 0], [1, -1]], [(0, 0), [0, -1], [0, 1], [-1, -1], [-1, 1]], [(0, 0), [-1, 0], [1, 0], [-1, 1], [1, 1]], [(0, 0), [0, -1], [0, 1], [1, -1], [1, 1]]],
                   [[(0, 0), [-1, 0], [-2, 0], [0, -1], [0, -2]], [(0, 0), [-1, 0], [-2, 0], [0, 1], [0, 2]], [(0, 0), [1, 0], [2, 0], [0, 1], [0, 2]], [(0, 0), [1, 0], [2, 0], [0, -1], [0, -2]]],
                   [[(0, 0), [0, 1], [-1, 1], [1, -1], [1, 0]], [(0, 0), [-1, -1], [0, -1], [1, 0], [1, 1]], [(0, 0), [-1, 0], [0, -1], [1, -1], [-1, 1]], [(0, 0), [-1, 0], [-1, -1], [1, 1], [0, 1]]],
                   [[(0, 0), [-1, 0], [0, -1], [1, 0], [0, 1]], [(0, 0), [-1, 0], [0, -1], [1, 0], [0, 1]], [(0, 0), [-1, 0], [0, -1], [1, 0], [0, 1]], [(0, 0), [-1, 0], [0, -1], [1, 0], [0, 1]]],
                   [[(0, 0), [-1, -1], [0, -1], [0, 1], [0, -2]], [(0, 0), [-1, 0], [-2, 0], [1, 0], [-1, 1]], [(0, 0), [1, 1], [0, 1], [0, -1], [0, 2]], [(0, 0), [1, -1], [1, 0], [-1, 0], [2, 0]]],
                   [[(0, 0), [0, -1], [-1, -1], [1, 1], [0, 1]], [(0, 0), [-1, 0], [1, 0], [1, -1], [-1, 1]], [(0, 0), [0, -1], [-1, -1], [1, 1], [0, 1]], [(0, 0), [-1, 0], [1, 0], [1, -1], [-1, 1]]]
                   ]

pieces_dictionary = {"one": [(0, 0)],
                     "two": [(0, 0), [1, 0]],
                     "three_i": [(0, 0), (-1, 0), (1, 0)],
                     "three_l": [(0, 0), (0, -1), (1, 0)],
                     "four_i": [(0, 0), (-1, 0), (1, 0), (2, 0)],
                     "four_l": [(0, 0), (0, -1), (0, 1), (1, 1)],
                     "four_o": [(0, 0), (-1, 0), (0, -1), (-1, -1)],
                     "four_s": [(0, 0), (0, -1), (1, 1), (1, 0)],
                     "four_t": [(0, 0), (0, 1), (1, 0), (-1, 0)],
                     "f_f": [(0, 0), (-1, 0), (0, -1), (1, -1), (0, 1)],
                     "f_i": [(0, 0), (-1, 0), (-2, 0), (1, 0), (2, 0)],
                     "f_l": [(0, 0), (0, 1), (0, -1), (0, -2), (1, 1)],
                     "f_n": [(0, 0), (0, 1), (0, 2), (1, 0), (1, -1)],
                     "f_p": [(0, 0), (0, 1), (0, -1), (1, -1), (1, 0)],
                     "f_t": [(0, 0), (0, 1), (0, -1), (-1, -1), (1, -1)],
                     "f_u": [(0, 0), (-1, 0), (-1, -1), (1, 0), (1, -1)],
                     "f_v": [(0, 0), (-1, 0), (-2, 0), (0, -1), (0, -2)],
                     "f_w": [(0, 0), (0, 1), (-1, 1), (1, -1), (1, 0)],
                     "f_x": [(0, 0), (-1, 0), (0, -1), (1, 0), (0, 1)],
                     "f_y": [(0, 0), (-1, 0), (0, -1), (0, 1), (0, 2)],
                     "f_z": [(0, 0), (0, -1), (-1, -1), (1, 1), (0, 1)]
                     }


review_board = [[0 for _ in range(5)] for _ in range(5)]
gameboard = [[0 for _ in range(20)] for _ in range(20)]
game_progression = []

font = "Cooper Black"
outline = "slateblue4"
color = ["white", "blue", "yellow", "red", "green", "cadetblue3", "lightgoldenrod1", "coral2", "seagreen2"]
turn = 1
score = 0

score_b = 0
score_y = 0
score_r = 0
score_g = 0
scores = [score_b, score_y, score_r, score_g]
selected_piece = None
mirrored = False

def start_window():
    def ai_mode(i):
        if i != "CHOOSE AI DIFFICULTY":
            start_button.configure(state=NORMAL)
        else:
            start_button.configure(state=DISABLED)

    def game_mode(i):
        start_button.configure(state=DISABLED)
        if i != "Singleplayer":
            ai_menu.configure(state=DISABLED)
            start_button.configure(state=NORMAL)

        else:
            if ai_clicked.get() != "CHOOSE AI DIFFICULTY":
                ai_menu.configure(state=NORMAL)
                start_button.configure(state=NORMAL)
            else:
                ai_menu.configure(state=NORMAL)
                start_button.configure(state=DISABLED)


    root = tk.Tk()
    root.title("BLOKUS GAME")
    root.geometry("400x400")
    root.resizable(False, False)

    canvas_blue = tk.Canvas(root, width=400, height=400, bg="crimson")
    canvas_blue.pack(fill=BOTH, expand=True)
    canvas = tk.Canvas(canvas_blue, width=400, height=400, bg="coral2")
    canvas.pack(fill="both", expand=YES, pady=10, padx=10)

    style = ttk.Style()
    style.configure("new.TButton", font=(font, 40), background="coral2", foreground="black")

    label1 = tk.Label(canvas, text="BLOKUS", font=(font, 40), bg="coral2", fg="black")
    label1.pack(pady=10)

    player_option_list = [
        "Singleplayer",
        "2 Players"
    ]
    player_clicked = StringVar()
    player_clicked.set("CHOOSE GAMEMODE")
    player_menu = tk.OptionMenu(canvas, player_clicked, *player_option_list, command=game_mode)
    player_menu.configure(width=20, font=(font, 10), bg=color[6], activebackground=color[6])
    player_menu.pack(side=tk.TOP, fill="none", padx=10, pady=10)

    ai_option_list = [
        "AI RANDOM",
        "AI LEVEL 1",
        "AI LEVEL 2"
    ]
    ai_clicked = StringVar()
    ai_clicked.set("CHOOSE AI DIFFICULTY")
    ai_menu = tk.OptionMenu(canvas, ai_clicked, *ai_option_list, command=ai_mode)
    ai_menu.configure(width=20, font=(font, 10), state=DISABLED, bg=color[6], activebackground=color[6])
    ai_menu.pack(side=tk.TOP, fill="none", padx=10, pady=10)

    chaos_selected = IntVar()
    chaos_mode_checkbox = tk.Checkbutton(canvas, text="CHAOS MODE", font=(font, 10), bg=color[6], variable=chaos_selected)
    chaos_mode_checkbox.pack(side=tk.TOP, pady=10)


    def main():
        root.withdraw()
        game = tk.Tk()
        game.geometry("900x900")
        game.minsize(width=600, height=600)
        game.title("BLOKUS")
        board = tk.Canvas(game, width=900, height=900, bg="lightcoral")
        board.grid(row=0, column=0, sticky=NW)
        board.pack(side=TOP, fill=BOTH, expand=YES)

        def evaluate():
            global eval_player, eval_ai
            eval_player = 0
            eval_ai = 0
            ais_val = (2, 4, -2, -4)
            players_val = (1, 3, -1, -3)
            for i in range(20):
                for j in range(20):
                    if gameboard[i][j] == players_val[0] or gameboard[i][j] == players_val[1]:
                        if 5 < i < 13 and 5 < j < 13:
                            eval_player += 2
                        elif 2 < i < 17 and 2 < j < 17 and 5 > i > 13 and 5 > j > 13:
                            eval_player += 1.5
                        else:
                            eval_player += 1
                    if gameboard[i][j] == players_val[2] or gameboard[i][j] == players_val[3]:
                        eval_player += 0.2

                    if gameboard[i][j] == ais_val[0] or gameboard[i][j] == ais_val[1]:
                        if 5 < i < 13 and 5 < j < 13:
                            eval_ai += 2
                        elif 2 < i < 17 and 2 < j < 17 and 5 > i > 13 and 5 > j > 13:
                            eval_ai += 1.5
                        else:
                            eval_ai += 1
                    if gameboard[i][j] == ais_val[2] or gameboard[i][j] == ais_val[3]:
                        eval_ai += 0.2
            return eval_player - eval_ai

        def ai_place(ai_x, ai_y, ai_mirrored, ai_selected_piece, ai_rotation):
            global turn, color, score
            if ai_selected_piece is not None:

                col = ai_x
                row = ai_y
                placeable = False
                score = 0

                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                counter = 0
                valid_corners = 0
                for i in range(20):
                    for j in range(20):
                        if gameboard[i][j] == -turn:
                            valid_corners += 1

                if ai_mirrored is True:
                    for x, y in piece_rotations[ai_selected_piece][ai_rotation]:
                        row_i = row + y
                        col_i = col - x
                        if row_i < 0 or row_i > 19 or col_i < 0 or col_i > 19:
                            # print("CAN NOT BE PLACED IN THE BOARD! TRY AGAIN!")
                            return None
                        if gameboard[row_i][col_i] == 0 or gameboard[row_i][col_i] == -1 or gameboard[row_i][
                            col_i] == -2 or \
                                gameboard[row_i][col_i] == -3 or gameboard[row_i][col_i] == -4:
                            continue
                        else:
                            # print("CAN NOT OVERLAP WITH OTHER PIECES! TRY AGAIN!")
                            return None
                else:
                    for x, y in piece_rotations[ai_selected_piece][ai_rotation]:
                        row_i = row + y
                        col_i = col + x
                        if row_i < 0 or row_i > 19 or col_i < 0 or col_i > 19:
                            # print("CAN NOT BE PLACED IN THE BOARD! TRY AGAIN!")
                            return None
                        if gameboard[row_i][col_i] == 0 or gameboard[row_i][col_i] == -1 or gameboard[row_i][
                            col_i] == -2 or \
                                gameboard[row_i][col_i] == -3 or gameboard[row_i][col_i] == -4:
                            continue
                        else:
                            # print("CAN NOT OVERLAP WITH OTHER PIECES! TRY AGAIN!")
                            return None

                if ai_mirrored is True:
                    for x, y in piece_rotations[ai_selected_piece][ai_rotation]:
                        row_l = row + y
                        col_l = col - x
                        if gameboard[row_l][col_l] == -turn:
                            counter += 1
                        else:
                            continue

                else:
                    for x, y in piece_rotations[ai_selected_piece][ai_rotation]:
                        row_l = row + y
                        col_l = col + x
                        # print(row_l, col_l)
                        if gameboard[row_l][col_l] == -turn:
                            counter += 1
                        else:
                            continue

                if counter == 0:
                    if ai_mirrored is True:
                        for x, y in piece_rotations[ai_selected_piece][ai_rotation]:
                            row_i = row + y
                            col_i = col - x
                            gameboard[row_i][col_i] = 0

                    else:
                        for x, y in piece_rotations[ai_selected_piece][ai_rotation]:
                            row_i = row + y
                            col_i = col + x
                            gameboard[row_i][col_i] = 0
                    # print("YOU ARE NOT TOUCHING ANY OF YOUR CORNERS! TRY AGAIN!")
                    return None

                # checks if other pieces of yours are being touched
                if ai_mirrored is True:
                    for x, y in piece_rotations[ai_selected_piece][ai_rotation]:
                        row_i = row + y
                        col_i = col - x
                        # Check the adjacent cells for 0
                        for d_x, d_y in directions:
                            adjacent_x, adjacent_y = col_i + d_x, row_i + d_y
                            if 20 > adjacent_x >= 0 and -1 <= adjacent_y < 20:
                                if gameboard[adjacent_y][adjacent_x] != turn:
                                    continue
                                else:
                                    # print("YOU ARE COLLIDING WITH ANOTHER PIECE OF YOURS! TRY AGAIN!")
                                    return None
                            else:
                                continue

                else:
                    for x, y in piece_rotations[ai_selected_piece][ai_rotation]:
                        row_i = row + y
                        col_i = col + x
                        # Check the adjacent cells for 0
                        for d_x, d_y in directions:
                            adjacent_x, adjacent_y = col_i + d_x, row_i + d_y
                            if 20 > adjacent_x >= 0 and -1 <= adjacent_y < 20:
                                if gameboard[adjacent_y][adjacent_x] != turn:
                                    continue
                                else:
                                    # print("YOU ARE COLLIDING WITH ANOTHER PIECE OF YOURS! TRY AGAIN!")
                                    return None
                            else:
                                continue

                if ai_mirrored is True:
                    for x, y in piece_rotations[ai_selected_piece][ai_rotation]:
                        row_i = row + y
                        col_i = col - x
                        gameboard[row_i][col_i] = turn

                else:
                    for x, y in piece_rotations[ai_selected_piece][ai_rotation]:
                        row_i = row + y
                        col_i = col + x
                        gameboard[row_i][col_i] = turn

                if turn == 1:
                    if gameboard[19][0] == -1:
                        if ai_mirrored is True:
                            for x, y in piece_rotations[ai_selected_piece][ai_rotation]:
                                row_i = row + y
                                col_i = col - x
                                gameboard[row_i][col_i] = 0

                        else:
                            for x, y in piece_rotations[ai_selected_piece][ai_rotation]:
                                row_i = row + y
                                col_i = col + x
                                gameboard[row_i][col_i] = 0

                        score = 0
                        # print("INVALID FIRST MOVE! TRY AGAIN!")
                        return None
                    else:
                        placeable = True
                if turn == 2:
                    if gameboard[0][0] == -2:
                        if ai_mirrored is True:
                            for x, y in piece_rotations[ai_selected_piece][ai_rotation]:
                                row_i = row + y
                                col_i = col - x
                                gameboard[row_i][col_i] = 0

                        else:
                            for x, y in piece_rotations[ai_selected_piece][ai_rotation]:
                                row_i = row + y
                                col_i = col + x
                                gameboard[row_i][col_i] = 0
                        score = 0
                        # print("INVALID FIRST MOVE! TRY AGAIN!")
                        return None
                    else:
                        placeable = True
                if turn == 3:
                    if gameboard[0][19] == -3:
                        if ai_mirrored is True:
                            for x, y in piece_rotations[ai_selected_piece][ai_rotation]:
                                row_i = row + y
                                col_i = col - x
                                gameboard[row_i][col_i] = 0

                        else:
                            for x, y in piece_rotations[ai_selected_piece][ai_rotation]:
                                row_i = row + y
                                col_i = col + x
                                gameboard[row_i][col_i] = 0
                        score = 0
                        # print("INVALID FIRST MOVE! TRY AGAIN!")
                        return None
                    else:
                        placeable = True
                if turn == 4:
                    if gameboard[19][19] == -4:
                        if ai_mirrored is True:
                            for x, y in piece_rotations[ai_selected_piece][ai_rotation]:
                                row_i = row + y
                                col_i = col - x
                                gameboard[row_i][col_i] = 0

                        else:
                            for x, y in piece_rotations[ai_selected_piece][ai_rotation]:
                                row_i = row + y
                                col_i = col + x
                                gameboard[row_i][col_i] = 0
                        score = 0
                        # print("INVALID FIRST MOVE! TRY AGAIN!")
                        return None
                    else:
                        placeable = True

                if placeable is True:
                    game_progression.append([ai_selected_piece, ai_mirrored, ai_rotation, color[turn], row, col])
                    print(game_progression)
                    selected_piece = None
                    rotate_counter = 0
                    mirrored = False
                    scoreboard(score)
                    draw()
                    turn += 1
                    if turn > 4:
                        turn = 1
                    canvas.delete("all")
                    draw()
            else:
                return None

        def ai_turn():
            global turn
            checked = []
            if turn == 2 or turn == 4:
                if player_clicked.get() == "Singleplayer":
                    if ai_clicked.get() == "AI RANDOM":
                        if turn == 2 or turn == 4:
                            while turn == 2 or turn == 4:
                                if turn == 2:
                                    if not piece_numbers_ai_y:
                                        turn += 1
                                        print("no more pieces left for yellow")
                                        board.delete("all")
                                        draw()
                                        return None
                                    ai_selected_piece = random.choice(piece_numbers_ai_y)
                                else:
                                    if not piece_numbers_ai_g:
                                        turn = 1
                                        print("no more pieces left for green")
                                        board.delete("all")
                                        draw()
                                        return None
                                    ai_selected_piece = random.choice(piece_numbers_ai_g)
                                ai_mirrored = random.randint(0, 1)
                                ai_rotate_counter = random.randint(0, 3)
                                if turn == 2:
                                    if ai_selected_piece not in piece_numbers_ai_y:
                                        continue
                                    if len(game_progression) < 4:
                                        ai_col = random.randint(0, 2)
                                        ai_row = random.randint(0, 2)
                                        checking = [ai_col, ai_row, ai_mirrored, ai_selected_piece, ai_rotate_counter]
                                        for check in range(len(checked)):
                                            if check == checking:
                                                continue
                                        ai_place(ai_col, ai_row, ai_mirrored, ai_selected_piece, ai_rotate_counter)
                                        if turn != 2:
                                            piece_numbers_ai_y.remove(ai_selected_piece)
                                        checked.append([ai_col, ai_row, ai_mirrored, ai_selected_piece, ai_rotate_counter])
                                    elif 4 < len(game_progression) < 20:
                                        ai_col = random.randint(0, 10)
                                        ai_row = random.randint(0, 10)
                                        checking = [ai_col, ai_row, ai_mirrored, ai_selected_piece, ai_rotate_counter]
                                        for check in range(len(checked)):
                                            if check == checking:
                                                continue
                                        ai_place(ai_col, ai_row, ai_mirrored, ai_selected_piece, ai_rotate_counter)
                                        if turn != 2:
                                            piece_numbers_ai_y.remove(ai_selected_piece)
                                        checked.append([ai_col, ai_row, ai_mirrored, ai_selected_piece, ai_rotate_counter])
                                    else:
                                        ai_col = random.randint(0, 17)
                                        ai_row = random.randint(0, 17)
                                        checking = [ai_col, ai_row, ai_mirrored, ai_selected_piece, ai_rotate_counter]
                                        for check in range(len(checked)):
                                            if check == checking:
                                                continue
                                        ai_place(ai_col, ai_row, ai_mirrored, ai_selected_piece, ai_rotate_counter)
                                        if turn != 2:
                                            piece_numbers_ai_y.remove(ai_selected_piece)
                                        checked.append([ai_col, ai_row, ai_mirrored, ai_selected_piece, ai_rotate_counter])
                                else:
                                    if ai_selected_piece not in piece_numbers_ai_g:
                                        continue
                                    if len(game_progression) < 4:
                                        ai_col = random.randint(17, 19)
                                        ai_row = random.randint(17, 19)
                                        checking = [ai_col, ai_row, ai_mirrored, ai_selected_piece, ai_rotate_counter]
                                        for check in range(len(checked)):
                                            if check == checking:
                                                continue
                                        ai_place(ai_col, ai_row, ai_mirrored, ai_selected_piece, ai_rotate_counter)
                                        if turn != 4:
                                            piece_numbers_ai_g.remove(ai_selected_piece)
                                        checked.append([ai_col, ai_row, ai_mirrored, ai_selected_piece, ai_rotate_counter])
                                    elif 4 < len(game_progression) < 20:
                                        ai_col = random.randint(10, 19)
                                        ai_row = random.randint(10, 19)
                                        checking = [ai_col, ai_row, ai_mirrored, ai_selected_piece, ai_rotate_counter]
                                        for check in range(len(checked)):
                                            if check == checking:
                                                continue
                                        ai_place(ai_col, ai_row, ai_mirrored, ai_selected_piece, ai_rotate_counter)
                                        if turn != 4:
                                            piece_numbers_ai_g.remove(ai_selected_piece)
                                        checked.append([ai_col, ai_row, ai_mirrored, ai_selected_piece, ai_rotate_counter])
                                    else:
                                        ai_col = random.randint(2, 19)
                                        ai_row = random.randint(2, 19)
                                        checking = [ai_col, ai_row, ai_mirrored, ai_selected_piece, ai_rotate_counter]
                                        for check in range(len(checked)):
                                            if check == checking:
                                                continue
                                        ai_place(ai_col, ai_row, ai_mirrored, ai_selected_piece, ai_rotate_counter)
                                        if turn != 4:
                                            piece_numbers_ai_g.remove(ai_selected_piece)
                                        checked.append([ai_col, ai_row, ai_mirrored, ai_selected_piece, ai_rotate_counter])

                                if len(checked) > 1000:
                                    game_progression.append([-1, f"TURN SKIPPED BY AI: <{color[turn]}> "])
                                    turn += 1
                                    if turn > 4:
                                        turn = 1
                                    board.delete("all")
                                    draw()
                                    return None

        def scoreboard(points):
            global score_y, score_b, score_r, score_g, turn, score
            if turn == 4:
                score_g += points
            elif turn == 3:
                score_r += points
            elif turn == 2:
                score_y += points
            else:
                score_b += points
            score = 0

        def draw():
            global score_b, score_y, score_r, score_g
            board.delete("all")
            sqsize = min(int(game.winfo_width()), int(game.winfo_height()))
            fontsize = sqsize // 50
            score_b = 0
            score_y = 0
            score_r = 0
            score_g = 0
            valid_corners = 0

            piece_size = sqsize / 45
            x_offset, y_offset = int(sqsize * 2 / 45), int(sqsize * 32 / 45)

            # draws the grid for the shapes
            """for row in range(15):
                for column in range(35):
                    board.create_rectangle(column * piece_size, row * piece_size + sqsize * 2 / 3,
                                          column * piece_size + piece_size, row * piece_size + piece_size + sqsize * 2 / 3,
                                          activefill="gray50")"""

            # draws separate canvas for the pieces
            board.create_rectangle(0, sqsize / 30 * 20, sqsize / 45 * 35, sqsize, fill="slateblue2", outline=outline)

            # draws the red lines
            for row in range(4):
                board.create_line(0, row * piece_size * 5 + sqsize * 2 / 3, sqsize * 7 / 9, row * piece_size * 5 + sqsize * 2 / 3, fill=outline, width=2)
                for column in range(8):
                    board.create_line(column * piece_size * 5, sqsize * 2 / 3, column * piece_size * 5, sqsize, fill=outline, width=2)

            # checks for a valid corner
            def check_surrounding_corners(valid_corners, x, y):
                # Define the possible directions for adjacent cells
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                # Check each corner
                for dx, dy in [(1, 1), (-1, 1), (-1, -1), (1, -1)]:
                    corner_x, corner_y = x + dx, y + dy
                    counter = 0
                    required_sides = 4
                    # Check if the corner is within the bounds of the board
                    if 20 > corner_x >= 0 and -1 <= corner_y < 20:
                        if gameboard[corner_y][corner_x] == 0:

                            # Check the adjacent cells for 0
                            for d_x, d_y in directions:
                                adjacent_x, adjacent_y = corner_x + d_x, corner_y + d_y
                                if 20 > adjacent_x >= 0 and -1 <= adjacent_y < 20:
                                    if gameboard[adjacent_y][adjacent_x] != turn:
                                        # Do something with the corner
                                        counter += 1
                                        # print(f"Corner at ({corner_x}, {corner_y}) has a neighboring 0.")
                                    else:
                                        break
                                else:
                                    required_sides -= 1
                                    continue
                                if required_sides == counter:
                                    gameboard[corner_y][corner_x] = -turn

                        else:
                            continue
                    else:
                        continue

            # draws the piece with the provided information from the function below
            def draw_piece(piece_number, x, y, piece_size, piece):
                if game_progression:
                    for cell in piece:
                        cell_x, cell_y = cell
                        board.create_rectangle(
                            x + cell_x * piece_size, y + cell_y * piece_size,
                            x + (cell_x + 1) * piece_size, y + (cell_y + 1) * piece_size,
                            fill=color[turn], outline=outline, tags="piece"
                        )
                    for t in range(len(game_progression)):
                        if t % 4 + 1 == turn:
                            if game_progression[t][0] == piece_number and game_progression[t][3] == color[turn]:
                                for cell in piece:
                                    cell_x, cell_y = cell
                                    board.create_rectangle(
                                        x + cell_x * piece_size, y + cell_y * piece_size,
                                        x + (cell_x + 1) * piece_size, y + (cell_y + 1) * piece_size,
                                        fill="gray60", outline=outline
                                )
                        else:
                            continue
                else:
                    for cell in piece:
                        cell_x, cell_y = cell
                        board.create_rectangle(
                            x + cell_x * piece_size, y + cell_y * piece_size,
                            x + (cell_x + 1) * piece_size, y + (cell_y + 1) * piece_size,
                            fill=color[turn], outline=outline, tags="piece"
                        )

            # sorts every piece into the grid and calls the draw function immediately after
            for piece_number, piece in enumerate(pieces):
                x = int(x_offset + (piece_number % 7) * piece_size * 5)
                y = int(y_offset + (piece_number // 7) * piece_size * 5)
                draw_piece(piece_number, x, y, piece_size, piece)

            # draws main board
            for row in range(20):
                for column in range(20):
                    if gameboard[row][column] == 1:
                        board.create_rectangle(column * sqsize / 30, row * sqsize / 30, column * sqsize / 30 + sqsize / 30,
                                               row * sqsize / 30 + sqsize / 30, fill="blue", tags="board", outline=outline)
                        score_b += 1
                    elif gameboard[row][column] == 2:
                        board.create_rectangle(column * sqsize / 30, row * sqsize / 30,
                                               column * sqsize / 30 + sqsize / 30,
                                               row * sqsize / 30 + sqsize / 30, fill="yellow", tags="board", outline=outline)
                        score_y += 1
                    elif gameboard[row][column] == 3:
                        board.create_rectangle(column * sqsize / 30, row * sqsize / 30, column * sqsize / 30 + sqsize / 30,
                                               row * sqsize / 30 + sqsize / 30, fill="red", tags="board", outline=outline)
                        score_r += 1
                    elif gameboard[row][column] == 4:
                        board.create_rectangle(column * sqsize / 30, row * sqsize / 30, column * sqsize / 30 + sqsize / 30,
                                               row * sqsize / 30 + sqsize / 30, fill="green", tags="board", outline=outline)
                        score_g += 1
                    else:
                        board.create_rectangle(column * sqsize / 30, row * sqsize / 30, column * sqsize / 30 + sqsize / 30, row * sqsize / 30 + sqsize / 30,
                                               fill="gray80", tags="board", outline=outline)

                    # Removes the valid corners from array except the one who is in turn
                    """if gameboard[row][column] <= -1:
                        if gameboard[row][column] == -turn:
                            continue
                        else:
                            gameboard[row][column] = 0"""

                    if gameboard[row][column] == turn:
                        check_surrounding_corners(valid_corners, column, row)

            # defaults every corner to the color index for its determined piece
            if gameboard[19][0] == 0:
                gameboard[19][0] = -1
            if gameboard[0][0] == 0:
                gameboard[0][0] = -2
            if gameboard[0][19] == 0:
                gameboard[0][19] = -3
            if gameboard[19][19] == 0:
                gameboard[19][19] = -4

            for row in range(20):
                for column in range(20):
                    if gameboard[row][column] == -turn:
                        board.create_oval(column * sqsize / 30, row * sqsize / 30, column * sqsize / 30 + sqsize / 30,
                                               row * sqsize / 30 + sqsize / 30, fill=color[turn + 4], tags="board", outline=outline)
                        valid_corners += 1
            # P - Keypress returns gameboard as array in console
            def print_gameboard(event=None):
                for r in gameboard:
                    print(r, end=" ")
                    print()
                print(valid_corners)
                print(selected_piece)
                print(eval_player, eval_ai)
                print(eval_player - eval_ai)

            # draws the scoreboard
            def draw_scoreboard():
                for y_icon in range(4):
                    board.create_rectangle(sqsize / 30 * 24.5, sqsize / 30 * 20 + y_icon * 2.5 * sqsize / 30 + sqsize / 30 * 0.5,
                                           sqsize / 30 * 26, sqsize / 30 * 20 + y_icon * 2.5 * sqsize / 30 + sqsize / 30 * 2, fill=color[y_icon + 1], width=3, outline=outline)
                    board.create_rectangle(sqsize / 30 * 26, sqsize / 30 * 20 + y_icon * 2.5 * sqsize / 30 + sqsize / 30 * 0.5,
                                           sqsize / 30 * 29, sqsize / 30 * 20 + y_icon * 2.5 * sqsize / 30 + sqsize / 30 * 2, width=3, outline=outline, fill="gray80")
                    if y_icon == 0:
                        board.create_text(sqsize / 30 * 27.5, sqsize / 30 * 21.25 + sqsize / 30 * y_icon * 2.5, text=f"{score_b}", font=(font, 30))
                    elif y_icon == 1:
                        board.create_text(sqsize / 30 * 27.5, sqsize / 30 * 21.25 + sqsize / 30 * y_icon * 2.5, text=f"{score_y}", font=(font, 30))
                    elif y_icon == 2:
                        board.create_text(sqsize / 30 * 27.5, sqsize / 30 * 21.25 + sqsize / 30 * y_icon * 2.5, text=f"{score_r}", font=(font, 30))
                    else:
                        board.create_text(sqsize / 30 * 27.5, sqsize / 30 * 21.25 + sqsize / 30 * y_icon * 2.5, text=f"{score_g}", font=(font, 30))

            # Click - Left mouse button press within the piece canvas draws the piece that was selected
            def draw_in_pb(event):
                if event.y < sqsize / 3 * 2 or event.x > sqsize / 9 * 7:
                    return None
                else:
                    global selected_piece, mirrored, rotate_counter
                    mirrored = False
                    rotate_counter = 0
                    row = int(event.y / (sqsize / 9))
                    col = int(event.x / (sqsize / 9))
                    # print(row, col)
                    if row >= 6:
                        if col > 6:
                            return None
                        else:
                            if row >= 7:
                                if col > 6:
                                    return None
                                if row >= 8:
                                    if col > 6:
                                        return None
                                    else:
                                        selected_piece = col + 14
                                else:
                                    selected_piece = col + 7
                            else:
                                selected_piece = col
                    if game_progression:
                        for t in range(len(game_progression)):
                            if t % 4 + 1 == turn:
                                if game_progression[t][0] == selected_piece and game_progression[t][3] == color[turn]:
                                    selected_piece = None
                                    draw()
                                    return None
                    draw()
                    return selected_piece

            # UNUSED FUNCTION
            def draw_array_rb():
                for row in review_board:
                    print(row, end=" ")
                    print()

            # draws the preview board
            def draw_pb():
                global selected_piece
                for row in range(7):
                    for column in range(7):
                        if row == 0:
                            board.create_rectangle(sqsize * 43 / 60 + column * sqsize / 30, sqsize * 1 / 30 + row * sqsize / 30,
                                                   sqsize * 45 / 60 + column * sqsize / 30, sqsize * 2 / 30 + row * sqsize / 30,
                                                   fill="lightpink3", outline="lightpink3", width=0)
                        elif row == 6:
                            board.create_rectangle(sqsize * 43 / 60 + column * sqsize / 30, sqsize * 1 / 30 + row * sqsize / 30,
                                                   sqsize * 45 / 60 + column * sqsize / 30, sqsize * 2 / 30 + row * sqsize / 30,
                                                   fill="lightpink3", outline="lightpink3", width=0)
                        elif column == 0:
                            board.create_rectangle(sqsize * 43 / 60 + column * sqsize / 30, sqsize * 1 / 30 + row * sqsize / 30,
                                                   sqsize * 45 / 60 + column * sqsize / 30, sqsize * 2 / 30 + row * sqsize / 30,
                                                   fill="lightpink3", outline="lightpink3", width=0)
                        elif column == 6:
                            board.create_rectangle(sqsize * 43 / 60 + column * sqsize / 30, sqsize * 1 / 30 + row * sqsize / 30,
                                                   sqsize * 45 / 60 + column * sqsize / 30, sqsize * 2 / 30 + row * sqsize / 30,
                                                   fill="lightpink3", outline="lightpink3", width=0)
                        else:
                            board.create_rectangle(sqsize * 43 / 60 + column * sqsize / 30, sqsize * 1 / 30 + row * sqsize / 30,
                                                   sqsize * 45 / 60 + column * sqsize / 30, sqsize * 2 / 30 + row * sqsize / 30, fill="lightpink4", outline=outline)
                board.create_line(sqsize / 30 * 22.5, sqsize / 30 * 7, sqsize / 30 * 27.5, sqsize / 30 * 7, fill=outline)
                board.create_line(sqsize / 30 * 27.5, sqsize / 30 * 2, sqsize / 30 * 27.5, sqsize / 30 * 7, fill=outline)
                board.create_line(sqsize / 30 * 21.5, sqsize / 30 * 1, sqsize / 30 * 28.5, sqsize / 30 * 1, fill=outline)
                board.create_line(sqsize / 30 * 21.5, sqsize / 30 * 8, sqsize / 30 * 28.5, sqsize / 30 * 8, fill=outline)
                board.create_line(sqsize / 30 * 21.5, sqsize / 30 * 1, sqsize / 30 * 21.5, sqsize / 30 * 8, fill=outline)
                board.create_line(sqsize / 30 * 28.5, sqsize / 30 * 1, sqsize / 30 * 28.5, sqsize / 30 * 8, fill=outline)

            # draws the piece inside the preview board
            def draw_piece_pb():
                global selected_piece
                x_offset = sqsize * 45 / 60
                y_offset = sqsize * 4 / 60
                if selected_piece is not None:
                    if mirrored is True:
                        if row == 0:
                            board.create_rectangle(sqsize * 21 / 30 + column * sqsize / 30,
                                                   sqsize * 1 / 30 + row * sqsize / 30,
                                                   sqsize * 22 / 30 + column * sqsize / 30,
                                                   sqsize * 2 / 30 + row * sqsize / 30,
                                                   fill="purple")
                        elif row == 6:
                            board.create_rectangle(sqsize * 21 / 30 + column * sqsize / 30,
                                                   sqsize * 1 / 30 + row * sqsize / 30,
                                                   sqsize * 22 / 30 + column * sqsize / 30,
                                                   sqsize * 2 / 30 + row * sqsize / 30,
                                                   fill="purple")
                        elif column == 0:
                            board.create_rectangle(sqsize * 21 / 30 + column * sqsize / 30,
                                                   sqsize * 1 / 30 + row * sqsize / 30,
                                                   sqsize * 22 / 30 + column * sqsize / 30,
                                                   sqsize * 2 / 30 + row * sqsize / 30,
                                                   fill="purple")
                        elif column == 6:
                            board.create_rectangle(sqsize * 21 / 30 + column * sqsize / 30,
                                                   sqsize * 1 / 30 + row * sqsize / 30,
                                                   sqsize * 22 / 30 + column * sqsize / 30,
                                                   sqsize * 2 / 30 + row * sqsize / 30,
                                                   fill="purple")
                        else:
                            piece_size = sqsize / 30
                            for x, y in piece_rotations[selected_piece][rotate_counter]:
                                board.create_rectangle((x_offset + (-x) * piece_size + piece_size * 2),
                                                       y_offset + y * piece_size + piece_size * 2,
                                                       (x_offset + piece_size * (-x) + piece_size * 3),
                                                       y_offset + piece_size * y + piece_size * 3,
                                                       fill=color[turn], outline=outline)
                    else:
                        if row == 0:
                            board.create_rectangle(sqsize * 21 / 30 + column * sqsize / 30, sqsize * 1 / 30 + row * sqsize / 30,
                                                   sqsize * 22 / 30 + column * sqsize / 30, sqsize * 2 / 30 + row * sqsize / 30,
                                                   fill="black")
                        elif row == 6:
                            board.create_rectangle(sqsize * 21 / 30 + column * sqsize / 30, sqsize * 1 / 30 + row * sqsize / 30,
                                                   sqsize * 22 / 30 + column * sqsize / 30, sqsize * 2 / 30 + row * sqsize / 30,
                                                   fill="black")
                        elif column == 0:
                            board.create_rectangle(sqsize * 21 / 30 + column * sqsize / 30, sqsize * 1 / 30 + row * sqsize / 30,
                                                   sqsize * 22 / 30 + column * sqsize / 30, sqsize * 2 / 30 + row * sqsize / 30,
                                                   fill="black")
                        elif column == 6:
                            board.create_rectangle(sqsize * 21 / 30 + column * sqsize / 30, sqsize * 1 / 30 + row * sqsize / 30,
                                                   sqsize * 22 / 30 + column * sqsize / 30, sqsize * 2 / 30 + row * sqsize / 30,
                                                   fill="black")
                        else:
                            piece_size = sqsize / 30
                            for x, y in piece_rotations[selected_piece][rotate_counter]:
                                board.create_rectangle(x_offset + x * piece_size + piece_size * 2, y_offset + y * piece_size + piece_size * 2,
                                                       x_offset + piece_size * x + piece_size * 3, y_offset + piece_size * y + piece_size * 3,
                                                       fill=color[turn], outline=outline)

            # R - Keypress rotates the piece clockwise (and while mirrored ccw)
            def rotate(event=None):
                global selected_piece, rotate_counter
                rotate_counter += 1
                if rotate_counter > 3:
                    rotate_counter = 0
                if selected_piece is not None:
                    board.delete("all")
                    draw()
                    hover(event)
                else:
                    return None

            # W - Keypress rotates the piece counterclockwise (and while mirrored clockwise)
            def rotate_ccw(event=None):
                global selected_piece, rotate_counter
                rotate_counter -= 1
                if rotate_counter < 0:
                    rotate_counter = 3

                if selected_piece is not None:
                    board.delete("all")
                    draw()
                    hover(event)
                else:
                    return None

            # E - Keypress mirrors the piece along the y-axis
            def mirror_piece(event=None):
                global mirrored
                if mirrored is False:
                    mirrored = True
                    board.delete("all")
                    draw()
                    hover(event)
                    return mirrored
                else:
                    mirrored = False
                    board.delete("all")
                    draw()
                    hover(event)
                    return mirrored

            # draws the buttons with text
            def draw_buttons():
                board.create_rectangle(sqsize * 21 / 30, sqsize * 22 / 72, sqsize * 29 / 30, sqsize * 27 / 72, fill=color[turn], outline=outline, width=3)
                board.create_rectangle(sqsize * 26 / 36, sqsize * 15 / 36, sqsize * 34 / 36, sqsize * 17 / 36, fill="gray75", activefill="lightgreen", tags="skip", outline=outline, width=3)
                board.create_rectangle(sqsize * 26 / 36, sqsize * 17 / 36, sqsize * 34 / 36, sqsize * 19 / 36, fill="gray75", activefill="lightgreen", tags="rules", outline=outline, width=3)
                board.create_rectangle(sqsize * 26 / 36, sqsize * 19 / 36, sqsize * 34 / 36, sqsize * 21 / 36, fill="gray75", activefill="lightgreen", tags="take_back", outline=outline, width=3)
                board.create_rectangle(sqsize * 26 / 36, sqsize * 21 / 36, sqsize * 34 / 36, sqsize * 23 / 36, fill="gray50", activefill="red", tags="quit", outline=outline, width=3)

                board.create_text(sqsize * 30 / 36, sqsize * 16 / 36, text="SKIP TURN", font=(font, fontsize), tags="skip", activefill="white")
                board.create_text(sqsize * 30 / 36, sqsize * 18 / 36, text="RULES", font=(font, fontsize), tags="rules", activefill="white")
                board.create_text(sqsize * 30 / 36, sqsize * 20 / 36, text="TAKE BACK", font=(font, fontsize), tags="take_back", activefill="white")
                board.create_text(sqsize * 30 / 36, sqsize * 22 / 36, text="END GAME", font=(font, fontsize), tags="quit", activefill="white")

            def hover(event=None):
                board.delete("all")
                draw()
                if event.x > sqsize / 3 * 2 or event.y > sqsize / 3 * 2:
                    return None
                else:
                    if selected_piece is not None:
                        grid = [[0 for _ in range(20)] for _ in range(20)]
                        col = int(event.x / (sqsize / 30))
                        row = int(event.y / (sqsize / 30))

                        if mirrored is True:
                            for x, y in piece_rotations[selected_piece][rotate_counter]:
                                row_i = row + y
                                col_i = col - x
                                if row_i < 0 or row_i > 19 or col_i < 0 or col_i > 19:
                                    return None

                        else:
                            for x, y in piece_rotations[selected_piece][rotate_counter]:
                                row_i = row + y
                                col_i = col + x
                                if row_i < 0 or row_i > 19 or col_i < 0 or col_i > 19:
                                    return None

                        if turn == 1:
                            hover_color = "cadetblue3"
                        elif turn == 2:
                            hover_color = "lightgoldenrod1"
                        elif turn == 3:
                            hover_color = "coral2"
                        else:
                            hover_color = "seagreen2"

                        if mirrored is True:
                            for x, y in piece_rotations[selected_piece][rotate_counter]:
                                row_i = row + y
                                col_i = col - x
                                grid[row_i][col_i] = turn

                        else:
                            for x, y in piece_rotations[selected_piece][rotate_counter]:
                                row_i = row + y
                                col_i = col + x
                                grid[row_i][col_i] = turn
                        for r in range(20):
                            for c in range(20):
                                if grid[r][c] == turn:
                                    board.create_rectangle(c * sqsize / 30, r * sqsize / 30,
                                                           c * sqsize / 30 + sqsize / 30,
                                                           r * sqsize / 30 + sqsize / 30,
                                                           fill=hover_color, tags="board", outline=outline)
                    else:
                        return None

            draw_scoreboard()
            draw_buttons()
            draw_pb()
            draw_piece_pb()
            evaluate()
            # draw_array_rb()

            board.bind("<Button-1>", draw_in_pb)
            board.bind("<Motion>", hover)
            game.bind("<p>", print_gameboard)
            game.bind("<w>", rotate)
            game.bind("<e>", mirror_piece)
            game.bind("<r>", rotate_ccw)

        # every resize of the window calls this function
        def config(event=None):
            board.delete("all")
            draw()

        # Click - left mouse button press checks if a piece has been selected,
        # if it placeable and if so draw it on the gameboard
        def on_place(event=None):
            global turn, selected_piece, rotate_counter, mirrored, color, score
            if selected_piece is not None:
                sqsize = min(int(game.winfo_width()), int(game.winfo_height()))

                col = int(event.x / (sqsize / 30))
                row = int(event.y / (sqsize / 30))
                placeable = False
                score = 0

                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                counter = 0
                valid_corners = 0
                for i in range(20):
                    for j in range(20):
                        if gameboard[i][j] == -turn:
                            valid_corners += 1

                if mirrored is True:
                    for x, y in piece_rotations[selected_piece][rotate_counter]:
                        row_i = row + y
                        col_i = col - x
                        if row_i < 0 or row_i > 19 or col_i < 0 or col_i > 19:
                            # print("CAN NOT BE PLACED IN THE BOARD! TRY AGAIN!")
                            return None
                        if gameboard[row_i][col_i] == 0 or gameboard[row_i][col_i] == -1 or gameboard[row_i][col_i] == -2 or gameboard[row_i][col_i] == -3 or gameboard[row_i][col_i] == -4:
                            continue
                        else:
                            # print("CAN NOT OVERLAP WITH OTHER PIECES! TRY AGAIN!")
                            return None
                else:
                    for x, y in piece_rotations[selected_piece][rotate_counter]:
                        row_i = row + y
                        col_i = col + x
                        if row_i < 0 or row_i > 19 or col_i < 0 or col_i > 19:
                            # print("CAN NOT BE PLACED IN THE BOARD! TRY AGAIN!")
                            return None
                        if gameboard[row_i][col_i] == 0 or gameboard[row_i][col_i] == -1 or gameboard[row_i][col_i] == -2 or gameboard[row_i][col_i] == -3 or gameboard[row_i][col_i] == -4:
                            continue
                        else:
                            print("CAN NOT OVERLAP WITH OTHER PIECES! TRY AGAIN!")
                            return None

                if mirrored is True:
                    for x, y in piece_rotations[selected_piece][rotate_counter]:
                        row_l = row + y
                        col_l = col - x
                        if gameboard[row_l][col_l] == -turn:
                            counter += 1
                        else:
                            continue

                else:
                    for x, y in piece_rotations[selected_piece][rotate_counter]:
                        row_l = row + y
                        col_l = col + x
                        # print(row_l, col_l)
                        if gameboard[row_l][col_l] == -turn:
                            counter += 1
                        else:
                            continue

                if counter == 0:
                    if mirrored is True:
                        for x, y in piece_rotations[selected_piece][rotate_counter]:
                            row_i = row + y
                            col_i = col - x
                            gameboard[row_i][col_i] = 0

                    else:
                        for x, y in piece_rotations[selected_piece][rotate_counter]:
                            row_i = row + y
                            col_i = col + x
                            gameboard[row_i][col_i] = 0
                    # print("YOU ARE NOT TOUCHING ANY OF YOUR CORNERS! TRY AGAIN!")
                    return None

                # checks if other pieces of yours are being touched
                if mirrored is True:
                    for x, y in piece_rotations[selected_piece][rotate_counter]:
                        row_i = row + y
                        col_i = col - x
                        # Check the adjacent cells for 0
                        for d_x, d_y in directions:
                            adjacent_x, adjacent_y = col_i + d_x, row_i + d_y
                            if 20 > adjacent_x >= 0 and -1 <= adjacent_y < 20:
                                if gameboard[adjacent_y][adjacent_x] != turn:
                                    continue
                                else:
                                    # print("YOU ARE COLLIDING WITH ANOTHER PIECE OF YOURS! TRY AGAIN!")
                                    return None
                            else:
                                continue

                else:
                    for x, y in piece_rotations[selected_piece][rotate_counter]:
                        row_i = row + y
                        col_i = col + x
                        # Check the adjacent cells for 0
                        for d_x, d_y in directions:
                            adjacent_x, adjacent_y = col_i + d_x, row_i + d_y
                            if 20 > adjacent_x >= 0 and -1 <= adjacent_y < 20:
                                if gameboard[adjacent_y][adjacent_x] != turn:
                                    continue
                                else:
                                    # print("YOU ARE COLLIDING WITH ANOTHER PIECE OF YOURS! TRY AGAIN!")
                                    return None
                            else:
                                continue

                if mirrored is True:
                    for x, y in piece_rotations[selected_piece][rotate_counter]:
                        row_i = row + y
                        col_i = col - x
                        gameboard[row_i][col_i] = turn

                else:
                    for x, y in piece_rotations[selected_piece][rotate_counter]:
                        row_i = row + y
                        col_i = col + x
                        gameboard[row_i][col_i] = turn

                if turn == 1:
                    if gameboard[19][0] == -1:
                        if mirrored is True:
                            for x, y in piece_rotations[selected_piece][rotate_counter]:
                                row_i = row + y
                                col_i = col - x
                                gameboard[row_i][col_i] = 0

                        else:
                            for x, y in piece_rotations[selected_piece][rotate_counter]:
                                row_i = row + y
                                col_i = col + x
                                gameboard[row_i][col_i] = 0

                        score = 0
                        # print("INVALID FIRST MOVE! TRY AGAIN!")
                        return None
                    else:
                        placeable = True
                if turn == 2:
                    if gameboard[0][0] == -2:
                        if mirrored is True:
                            for x, y in piece_rotations[selected_piece][rotate_counter]:
                                row_i = row + y
                                col_i = col - x
                                gameboard[row_i][col_i] = 0

                        else:
                            for x, y in piece_rotations[selected_piece][rotate_counter]:
                                row_i = row + y
                                col_i = col + x
                                gameboard[row_i][col_i] = 0
                        score = 0
                        # print("INVALID FIRST MOVE! TRY AGAIN!")
                        return None
                    else:
                        placeable = True
                if turn == 3:
                    if gameboard[0][19] == -3:
                        if mirrored is True:
                            for x, y in piece_rotations[selected_piece][rotate_counter]:
                                row_i = row + y
                                col_i = col - x
                                gameboard[row_i][col_i] = 0

                        else:
                            for x, y in piece_rotations[selected_piece][rotate_counter]:
                                row_i = row + y
                                col_i = col + x
                                gameboard[row_i][col_i] = 0
                        score = 0
                        # print("INVALID FIRST MOVE! TRY AGAIN!")
                        return None
                    else:
                        placeable = True
                if turn == 4:
                    if gameboard[19][19] == -4:
                        if mirrored is True:
                            for x, y in piece_rotations[selected_piece][rotate_counter]:
                                row_i = row + y
                                col_i = col - x
                                gameboard[row_i][col_i] = 0

                        else:
                            for x, y in piece_rotations[selected_piece][rotate_counter]:
                                row_i = row + y
                                col_i = col + x
                                gameboard[row_i][col_i] = 0
                        score = 0
                        # print("INVALID FIRST MOVE! TRY AGAIN!")
                        return None
                    else:
                        placeable = True

                if placeable is True:
                    game_progression.append([selected_piece, mirrored, rotate_counter, color[turn], row, col])
                    print(game_progression)
                    selected_piece = None
                    rotate_counter = 0
                    mirrored = False
                    scoreboard(score)
                    draw()
                    turn += 1
                    if turn > 4:
                        turn = 1
                    canvas.delete("all")
                    draw()
                    if turn == 2 or turn == 4:
                        ai_turn()
            else:
                return None

        # CANVAS BUTTON - left mouse button click skips turn manually
        def skip_turn(event=None):
            global turn, selected_piece, mirrored, rotate_counter
            game_progression.append([-1, f"TURN SKIPPED BY: <{color[turn]}> "])
            turn += 1
            if turn > 4:
                turn = 1
            canvas.delete("all")
            selected_piece = None
            mirrored = False
            rotate_counter = 0
            print(game_progression)
            draw()
            if turn == 2 or turn == 4:
                ai_turn()

        # CANVAS BUTTON - left mouse button click takes back one move
        def take_back(event=None):
            global turn, selected_piece, rotate_counter, mirrored, score
            if not game_progression:
                return None
            else:
                if game_progression[-1][0] == -1:
                    turn -= 1
                    if turn < 1:
                        turn = 4
                    game_progression.pop()
                else:
                    selected_piece = game_progression[-1][0]
                    mirrored = game_progression[-1][1]
                    rotate_counter = game_progression[-1][2]

                    row = game_progression[-1][4]
                    col = game_progression[-1][5]

                    if mirrored is True:
                        for x, y in piece_rotations[selected_piece][rotate_counter]:
                            row_i = row + y
                            col_i = col - x
                            gameboard[row_i][col_i] = 0
                            if turn == 4:
                                if row_i == 19 and col_i == 19:
                                    gameboard[row_i][col_i] = -4
                            elif turn == 3:
                                if row_i == 0 and col_i == 19:
                                    gameboard[row_i][col_i] = -3
                            elif turn == 2:
                                if row_i == 0 and col_i == 0:
                                    gameboard[row_i][col_i] = -2
                            elif turn == 1:
                                if row_i == 19 and col_i == 0:
                                    gameboard[row_i][col_i] = -1
                            score -= 1
                    else:
                        for x, y in piece_rotations[selected_piece][rotate_counter]:
                            row_i = row + y
                            col_i = col + x
                            try:
                                gameboard[row_i][col_i] = 0
                            except IndexError:
                                 print("NOT IN GAMEBOARD")

                            if turn == 4:
                                if row_i == 19 and col_i == 19:
                                    gameboard[row_i][col_i] = -4
                            elif turn == 3:
                                if row_i == 0 and col_i == 19:
                                    gameboard[row_i][col_i] = -3
                            elif turn == 2:
                                if row_i == 0 and col_i == 0:
                                    gameboard[row_i][col_i] = -2
                            elif turn == 1:
                                if row_i == 19 and col_i == 0:
                                    gameboard[row_i][col_i] = -1
                            score -= 1
                    turn -= 1
                    if turn < 1:
                        turn = 4
                    game_progression.pop()
            if not game_progression:
                gameboard[19][0] = -1

            print(game_progression)
            scoreboard(score)
            selected_piece = None
            rotate_counter = 0
            mirrored = False
            canvas.delete("all")
            draw()
            if player_clicked.get() == "Singleplayer":
                if turn == 2 or turn == 4:
                    take_back()
                    selected_piece = None
                    rotate_counter = 0
                    mirrored = False
                    board.delete("all")
                    draw()

        # CANVAS BUTTON - left mouse button click opens rules menu with all the important information to play
        def rules_menu(event):
            global rules

            def rules_next(event):
                r_canvas.delete("all")
                r_canvas.create_text(window_sqsize * 9 / window_grid, window_sqsize * 1 / window_grid, text="CORE RULES",
                                     font=(font, 30))
                r_canvas.create_rectangle(window_sqsize * 0.5 / window_grid, window_sqsize * 16 / window_grid,
                                          window_sqsize * 4.5 / window_grid, window_sqsize * 17 / window_grid,
                                          fill="gray75", activefill="lightgreen", tags="previous")
                r_canvas.create_rectangle(window_sqsize * 14 / window_grid, window_sqsize * 16 / window_grid,
                                          window_sqsize * 17 / window_grid, window_sqsize * 17 / window_grid,
                                          fill="gray75", activefill="lightgreen", tags="close")
                r_canvas.create_text(window_sqsize * 31 / window_grid / 2, window_sqsize * 35 / window_grid / 2, text="PAGE 2/2", font=(font, 15))
                r_canvas.create_text(window_sqsize * 5 / window_grid / 2, window_sqsize * 33 / window_grid / 2,
                                     text="PREVIOUS", font=(font, 15), tags="previous", activefill="white")
                r_canvas.create_text(window_sqsize * 31 / window_grid / 2, window_sqsize * 33 / window_grid / 2,
                                     text="CLOSE", font=(font, 15), tags="close", activefill="white")
                r_canvas.create_text(window_sqsize * 1 / window_grid, window_sqsize * 4.5 / window_grid,
                                     text="Every player starts on 0 points. The play order starts with blue at the bottom"
                                          " left side of the board. The turns go clockwise continuing with yellow, red and"
                                          " then green before blue goes again. There are the same 21 pieces for every color"
                                          " to play with. You pick a piece and place it on the board accordingly in order"
                                          " to get points. The points consist of the number of individual squares the piece"
                                          " is made of."
                                          "while all the 2-Player-Rules apply.", font=(font, 12), width=500,
                                     anchor="w")
                r_canvas.create_text(window_sqsize * 9 / window_grid, window_sqsize * 8 / window_grid, text="RULES TO PLACE",
                                     font=(font, 30))
                r_canvas.create_text(window_sqsize * 1 / window_grid, window_sqsize * 11.5 / window_grid,
                                     text="-- [1st MOVE] -- The piece must cover the corner.\n"
                                          "(Blue -> Bottom left; Yellow -> Upper left; Red -> Upper right; Green -> Bottom right\n"
                                          "-- The piece must be fully placeable on the board\n"
                                          "-- The piece must not overwrite another piece at all\n"
                                          "-- The piece must touch another piece of the same color but only on at least one corner\n"
                                          "-- The piece can touch differently colored pieces freely",
                                     font=(font, 12), width=500, anchor="w")

            def rules_previous(event):
                r_canvas.delete("all")
                r_canvas.create_text(window_sqsize * 9 / window_grid, window_sqsize * 1 / window_grid, text="CASUAL RULES",
                                     font=(font, 30))
                r_canvas.create_text(window_sqsize * 1 / window_grid, window_sqsize * 3 / window_grid,
                                     text="Singleplayer Rules: This can only be played against an AI.\n"
                                          "You choose the AI difficulty via Menu beforehand.\n"
                                          "The game is a standartized 2-Player game \n"
                                          "while all the 2-Player-Rules apply.", font=(font, 12), width=500,
                                     anchor="w")
                r_canvas.create_text(window_sqsize * 1 / window_grid, window_sqsize * 6 / window_grid,
                                     text="2-Players: Every player controls two colors.\n"
                                          "One player controls blue and red while\n the other controls yellow and green.\n"
                                          "Both colors of each player count towards their total points. The playing order remains the same."
                                     , font=(font, 12), width=500, anchor="w")
                r_canvas.create_rectangle(window_sqsize * 14 / window_grid, window_sqsize * 16 / window_grid,
                                          window_sqsize * 17 / window_grid, window_sqsize * 17 / window_grid,
                                          fill="gray75", activefill="lightgreen", tags="next")
                r_canvas.create_text(window_sqsize * 31 / window_grid / 2, window_sqsize * 35 / window_grid / 2,
                                     text="PAGE 1/2", font=(font, 15))
                r_canvas.create_text(window_sqsize * 31 / window_grid / 2, window_sqsize * 33 / window_grid / 2,
                                     text="NEXT", font=(font, 15), tags="next", activefill="white")
                r_canvas.create_text(window_sqsize * 9 / window_grid, window_sqsize * 8.5 / window_grid, text=font,
                                     font=(font, 30))
                r_canvas.create_text(window_sqsize * 1 / window_grid, window_sqsize * 10 / window_grid,
                                     text="[LEFT MB] - Hover over a piece and click to select it. Place it on the board via click.",
                                     font=(font, 12), width=500, anchor="w")
                r_canvas.create_text(window_sqsize * 1 / window_grid, window_sqsize * 14 / window_grid,
                                     text="[R] - Rotate the selected piece by 90° clockwise.",
                                     font=(font, 12), width=500, anchor="w")
                r_canvas.create_text(window_sqsize * 1 / window_grid, window_sqsize * 12.5 / window_grid,
                                     text="[E] - Emulate the selected piece in mirrored form along the Y-AXIS. BE AWARE THAT THE"
                                          " ROTATE BUTTONS CHANGE DIRECTIONS WHILE THE PIECE IS MIRRORED!",
                                     font=(font, 12), width=500, anchor="w")
                r_canvas.create_text(window_sqsize * 1 / window_grid, window_sqsize * 11 / window_grid,
                                     text="[W] - Rotate the selected piece by 90° counterclockwise.",
                                     font=(font, 12), width=500, anchor="w")
                r_canvas.create_text(window_sqsize * 1 / window_grid, window_sqsize * 15 / window_grid,
                                     text="[P] - Print the gameboard as an array via press.",
                                     font=(font, 12), width=500, anchor="w")
            def close_menu(event):
                rules.withdraw()

            rules = tk.Tk()
            rules.title("RULES")
            rules.resizable(False, False)
            r_canvas = tk.Canvas(rules, width=600, height=600, bg="lightcoral")
            r_canvas.pack()
            window_sqsize = 600
            window_grid = 18

            r_canvas.create_text(window_sqsize * 9 / window_grid, window_sqsize * 1 / window_grid, text="CASUAL RULES", font=(font, 30))
            r_canvas.create_text(window_sqsize * 1 / window_grid, window_sqsize * 3 / window_grid, text="Singleplayer Rules: This can only be played against an AI.\n"
                                                                                                        "You choose the AI difficulty via Menu beforehand.\n"
                                                                                                        "The game is a standartized 2-Player game \n"
                                                                                                        "while all the 2-Player-Rules apply.", font=(font, 12), width=500, anchor="w")
            r_canvas.create_text(window_sqsize * 1 / window_grid, window_sqsize * 6 / window_grid, text="2-Players: Every player controls two colors.\n"
                                                                                                        "One player controls blue and red while\n the other controls yellow and green.\n"
                                                                                                        "Both colors of each player count towards their total points. The playing order remains the same."
                                                                                                        , font=(font, 12), width=500, anchor="w")
            r_canvas.create_rectangle(window_sqsize * 14 / window_grid, window_sqsize * 16 / window_grid, window_sqsize * 17 / window_grid, window_sqsize * 17 / window_grid, fill="gray75", activefill="lightgreen", tags="next")
            r_canvas.create_text(window_sqsize * 9 / window_grid, window_sqsize * 8.5 / window_grid, text="KEYBINDS",
                                 font=(font, 30))
            r_canvas.create_text(window_sqsize * 1 / window_grid, window_sqsize * 10 / window_grid, text="[LEFT MB] - Hover over a piece and click to select it. Place it on the board via click.",
                                 font=(font, 12), width=500, anchor="w")
            r_canvas.create_text(window_sqsize * 1 / window_grid, window_sqsize * 14 / window_grid,
                                 text="[R] - Rotate the selected piece by 90° clockwise.",
                                 font=(font, 12), width=500, anchor="w")
            r_canvas.create_text(window_sqsize * 1 / window_grid, window_sqsize * 12.5 / window_grid,
                                 text="[E] - Emulate the selected piece in mirrored form along the Y-AXIS. BE AWARE THAT THE"
                                      " ROTATE BUTTONS CHANGE DIRECTIONS WHILE THE PIECE IS MIRRORED!",
                                 font=(font, 12), width=500, anchor="w")
            r_canvas.create_text(window_sqsize * 1 / window_grid, window_sqsize * 11 / window_grid,
                                 text="[W] - Rotate the selected piece by 90° counterclockwise.",
                                 font=(font, 12), width=500, anchor="w")
            r_canvas.create_text(window_sqsize * 1 / window_grid, window_sqsize * 15 / window_grid,
                                 text="[P] - Print the gameboard as an array via press.",
                                 font=(font, 12), width=500, anchor="w")
            r_canvas.create_text(window_sqsize * 31 / window_grid / 2, window_sqsize * 35 / window_grid / 2,
                                 text="PAGE 1/2", font=(font, 15))
            r_canvas.create_text(window_sqsize * 31 / window_grid / 2, window_sqsize * 33 / window_grid / 2,
                                 text="NEXT", font=(font, 15), tags="next", activefill="white")
            r_canvas.tag_bind("next", "<Button-1>", rules_next)
            r_canvas.tag_bind("previous", "<Button-1>", rules_previous)
            r_canvas.tag_bind("close", "<Button-1>", close_menu)
            rules.mainloop()

        # CANVAS BUTTON - left mouse button click ends the application
        def quit(event):
            global gameboard, game_progression, turn, selected_piece, mirrored, score_y, score_r, score_g, score_b, piece_numbers_ai_y, piece_numbers_ai_g
            game.withdraw()
            end_window = tk.Tk()
            end_window.geometry("400x500")
            end_window.resizable(False, False)
            screen = tk.Canvas(end_window, width=400, height=400, bg="coral2")
            screen.pack(fill=BOTH, expand=True)

            piece_size = 400
            piece_size = 300 // 20

            green = 0
            blue = 0
            yellow = 0
            red = 0

            win = ""

            for row in range(20):
                for column in range(20):
                    if gameboard[row][column] == 1:
                        blue += 1
                    elif gameboard[row][column] == 2:
                        yellow += 1
                    elif gameboard[row][column] == 3:
                        red += 1
                    elif gameboard[row][column] == 4:
                        green += 1
                    else:
                        continue

            if player_clicked.get() == "Singleplayer":
                player = blue + red
                ai = yellow + green
                winner = max(player, ai)

                if player == ai:
                    win = "NOBODY WON!"
                elif winner == player:
                    win = "YOU WON!"
                elif winner == ai:
                    win = "THE AI WON!"
                else:
                    win = "IT'S A DRAW!"
            else:
                winner = max(red, green, blue, yellow)

                if winner == score_b:
                    win = "BLUE WON!"
                elif winner == yellow:
                    win = "YELLOW WON!"
                elif winner == red:
                    win = "RED WON!"
                elif winner == green:
                    win = "GREEN WON!"

            def play_again():
                global gameboard, game_progression, turn, selected_piece, mirrored, score_y, score_r, score_g, score_b, piece_numbers_ai_y, piece_numbers_ai_g
                gameboard = [[0 for _ in range(20)] for _ in range(20)]
                game_progression = []
                turn = 1
                score_b = 0
                score_y = 0
                score_r = 0
                score_g = 0
                piece_numbers_ai_y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
                piece_numbers_ai_g = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
                selected_piece = None
                mirrored = False
                player_clicked.set("CHOOSE GAMEMODE")
                ai_clicked.set("CHOOSE AI DIFFICULTY")
                end_window.withdraw()
                start_window()

            def close():
                root.destroy()
                game.destroy()
                end_window.destroy()

            for row in range(20):
                for column in range(20):
                    if gameboard[row][column] == 1:
                        screen.create_rectangle(column * piece_size + 50, row * piece_size + 20,
                                                column * piece_size + 50 + piece_size, row * piece_size + 20 + piece_size,
                                                fill=color[1+4], tags="board", outline=outline)
                    elif gameboard[row][column] == 2:
                        screen.create_rectangle(column * piece_size + 50, row * piece_size + 20,
                                                column * piece_size + 50 + piece_size, row * piece_size + 20 + piece_size,
                                                fill=color[2+4], tags="board", outline=outline)
                    elif gameboard[row][column] == 3:
                        screen.create_rectangle(column * piece_size + 50, row * piece_size + 20,
                                                column * piece_size + 50 + piece_size, row * piece_size + 20 + piece_size,
                                                fill=color[3+4], tags="board", outline=outline)
                    elif gameboard[row][column] == 4:
                        screen.create_rectangle(column * piece_size + 50, row * piece_size + 20,
                                                column * piece_size + 50 + piece_size, row * piece_size + 20 + piece_size,
                                                fill=color[4+4], tags="board", outline=outline)
                    else:
                        screen.create_rectangle(column * piece_size + 50, row * piece_size + 20,
                                                column * piece_size + 50 + piece_size, row * piece_size + 20 + piece_size,
                                                fill="gray90", tags="board", outline=outline)

            screen.create_text(200, 170, font=(font, 30), text=f"GG!\n {win}", fill="crimson", width=300, justify="center")

            close_button = tk.Button(screen, text="CLOSE GAME", font=(font, 25), command=close, width=12)
            close_button.pack(side=tk.BOTTOM, pady=15)

            restart_button = tk.Button(screen, text="PLAY AGAIN", font=(font, 25), command=play_again, width=12)
            restart_button.pack(side=tk.BOTTOM)

            end_window.mainloop()

        # Calls draw function for the first time
        draw()

        board.tag_bind("board", "<Button-1>", on_place)
        board.tag_bind("skip", "<Button-1>", skip_turn)
        board.tag_bind("rules", "<Button-1>", rules_menu)
        board.tag_bind("take_back", "<Button-1>", take_back)
        board.tag_bind("quit", "<Button-1>", quit)

        # Every change in the window calls config function
        game.bind("<Configure>", config)
        game.mainloop()

    start_button = tk.Button(canvas, text="START GAME", font=(font, 25), command=main, width=12, state=DISABLED)
    start_button.pack(side=tk.BOTTOM, pady=30)

    root.bind("<o>", lambda event: print(chaos_selected.get()))

    root.mainloop()


start_window()
"""
WORKING ON THE RANDOM AI SO IT DOES NOT
REUSE PIECES IT ALREADY USED.
"""