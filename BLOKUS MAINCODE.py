import tkinter as tk
from tkinter import *
from progression import *
# import random

piece_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
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

for x in range(len(pieces)):
    print(pieces[x])

review_board = [[0 for _ in range(5)] for _ in range(5)]
gameboard = [[0 for _ in range(20)] for _ in range(20)]

color = ["blue", "yellow", "red", "green"]

turn = 0
score_b = 0
score_y = 0
score_r = 0
score_g = 0

selected_piece = None

root = tk.Tk()
root.title("BLOKUS GAME")
root.geometry("400x400")
root.resizable(width=NO, height=NO)

canvas_blue = tk.Canvas(root, width=400, height=400, bg="blue")
canvas_blue.pack(fill="both", expand=YES)
canvas = tk.Canvas(canvas_blue, width=400, height=400, bg="lightblue")
canvas.pack(fill="both", expand=YES, pady=10, padx=10)

label1 = tk.Label(canvas, text="BLOKUS", font=("Showcard Gothic", 40), bg="lightblue", fg="white")
label1.pack(pady=10)

player_option_list = [
    "Singleplayer",
    "2 Players"
]
player_clicked = StringVar()
player_clicked.set("CHOOSE GAMEMODE")
player_menu = tk.OptionMenu(canvas, player_clicked, *player_option_list)
player_menu.configure(width=20, font=("Showcard Gothic", 10))
player_menu.pack(side=tk.TOP, fill="none", padx=10, pady=10)

ai_option_list = [
    "NO AI (if not 1P)",
    "AI RANDOM",
    "AI LEVEL 1"
]
ai_clicked = StringVar()
ai_clicked.set("CHOOSE AI DIFFICULTY")
ai_menu = tk.OptionMenu(canvas, ai_clicked, *ai_option_list)
ai_menu.configure(width=20, font=("Showcard Gothic", 10))
ai_menu.pack(side=tk.TOP, fill="none", padx=10, pady=10)

chaos_mode_checkbox = tk.Checkbutton(canvas, text="CHAOS MODE", font=("Showcard Gothic", 10), state=DISABLED)
chaos_mode_checkbox.pack(side=tk.TOP, pady=10)


def main():
    root.withdraw()
    game = tk.Tk()
    game.geometry("900x900")
    game.minsize(width=600, height=600)
    game.title("BLOKUS")
    board = tk.Canvas(game, width=900, height=900, bg="lightgreen")
    board.grid(row=0, column=0, sticky=NW)
    board.pack(side=TOP, fill=BOTH, expand=YES)

    def draw():
        canvas.delete("all")
        sqsize = min(int(game.winfo_width()), int(game.winfo_height()))
        fontsize = sqsize // 50

        piece_size = sqsize / 45
        x_offset, y_offset = int(sqsize * 2 / 45), int(sqsize * 32 / 45)

        # draws the grid for the shapes
        for row in range(15):
            for column in range(35):
                board.create_rectangle(column * piece_size, row * piece_size + sqsize * 2 / 3,
                                      column * piece_size + piece_size, row * piece_size + piece_size + sqsize * 2 / 3,
                                      activefill="gray50")

        # draws the red lines
        for row in range(4):
            board.create_line(0, row * piece_size * 5 + sqsize * 2 / 3, sqsize * 7 / 9, row * piece_size * 5 + sqsize * 2 / 3, fill="red", width=1)
            for column in range(8):
                board.create_line(column * piece_size * 5, sqsize * 2 / 3, column * piece_size * 5, sqsize, fill="red", width=1)

        def draw_piece(piece_number, x, y, piece_size, piece):
            for cell in piece:
                cell_x, cell_y = cell
                board.create_rectangle(
                    x + cell_x * piece_size, y + cell_y * piece_size,
                    x + (cell_x + 1) * piece_size, y + (cell_y + 1) * piece_size,
                    fill=color[0], outline='black', tags="piece"
                )
                # print(piece_numbers[piece_number])

        for piece_number, piece in enumerate(pieces):
            x = int(x_offset + (piece_number % 7) * piece_size * 5)
            y = int(y_offset + (piece_number // 7) * piece_size * 5)
            draw_piece(piece_number, x, y, piece_size, piece)

        # draws main board
        for row in range(20):
            for column in range(20):
                if gameboard[row][column] == 1:
                    board.create_rectangle(column * sqsize / 30, row * sqsize / 30, column * sqsize / 30 + sqsize / 30,
                                           row * sqsize / 30 + sqsize / 30, fill="blue", tags="board")
                elif gameboard[row][column] == 2:
                    board.create_rectangle(column * sqsize / 30, row * sqsize / 30,
                                           column * sqsize / 30 + sqsize / 30,
                                           row * sqsize / 30 + sqsize / 30, fill="yellow", tags="board")
                elif gameboard[row][column] == 3:
                    board.create_rectangle(column * sqsize / 30, row * sqsize / 30, column * sqsize / 30 + sqsize / 30,
                                           row * sqsize / 30 + sqsize / 30, fill="red", tags="board")
                elif gameboard[row][column] == 4:
                    board.create_rectangle(column * sqsize / 30, row * sqsize / 30, column * sqsize / 30 + sqsize / 30,
                                           row * sqsize / 30 + sqsize / 30, fill="green", tags="board")
                else:
                    board.create_rectangle(column * sqsize / 30, row * sqsize / 30, column * sqsize / 30 + sqsize / 30, row * sqsize / 30 + sqsize / 30, fill="white", tags="board")

        def draw_in_pb(event):
            global selected_piece
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
            draw()
            return selected_piece

        def draw_array():
            for row in gameboard:
                print(row, end=" ")
                print()

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
                        board.create_rectangle(sqsize * 21 / 30 + column * sqsize / 30, sqsize * 1 / 30 + row * sqsize / 30,
                                               sqsize * 22 / 30 + column * sqsize / 30, sqsize * 2 / 30 + row * sqsize / 30, fill="gray50")

        def draw_piece_pb():
            global selected_piece
            x_offset = sqsize * 22 / 30
            y_offset = sqsize * 2 / 30
            if selected_piece is not None:
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
                                               fill="blue", outline="black")

        def rotate(event=None):
            global selected_piece, rotate_counter
            x_offset = sqsize * 22 / 30
            y_offset = sqsize * 2 / 30
            piece_size = sqsize / 30
            rotate_counter += 1
            if rotate_counter > 3:
                rotate_counter = 0
            if selected_piece is not None:
                canvas.delete("all")
                draw()
            else:
                return None

        board.create_rectangle(sqsize * 21 / 30, sqsize * 12 / 36, sqsize * 29 / 30, sqsize * 14 / 36, fill=color[0])
        board.create_rectangle(sqsize * 26 / 36, sqsize * 15 / 36, sqsize * 34 / 36, sqsize * 17 / 36, fill="gray75", activefill="lightgreen", tags="skip")
        board.create_rectangle(sqsize * 26 / 36, sqsize * 17 / 36, sqsize * 34 / 36, sqsize * 19 / 36, fill="gray75", activefill="lightgreen", tags="rules")
        board.create_rectangle(sqsize * 26 / 36, sqsize * 19 / 36, sqsize * 34 / 36, sqsize * 21 / 36, fill="gray75", activefill="lightgreen", tags="take_back")
        board.create_rectangle(sqsize * 26 / 36, sqsize * 21 / 36, sqsize * 34 / 36, sqsize * 23 / 36, fill="gray50", activefill="red", tags="quit")

        board.create_text(sqsize * 30 / 36, sqsize * 16 / 36, text="SKIP TURN", font=("Showcard Gothic", fontsize), tags="skip", activefill="white")
        board.create_text(sqsize * 30 / 36, sqsize * 18 / 36, text="RULES", font=("Showcard Gothic", fontsize), tags="rules", activefill="white")
        board.create_text(sqsize * 30 / 36, sqsize * 20 / 36, text="TAKE BACK", font=("Showcard Gothic", fontsize), tags="take_back", activefill="white")
        board.create_text(sqsize * 30 / 36, sqsize * 22 / 36, text="QUIT GAME", font=("Showcard Gothic", fontsize), tags="quit", activefill="white")

        draw_pb()
        draw_piece_pb()
        #draw_array()
        #draw_array_rb()

        board.bind("<Button-1>", draw_in_pb)
        game.bind("<r>", rotate)

    def config(event=None):
        board.delete("all")
        draw()


    def on_place(event):
        global turn, selected_piece, rotate_counter
        if selected_piece is not None:
            sqsize = min(int(game.winfo_width()), int(game.winfo_height()))
            canvas = event.widget
            item_id = canvas.find_closest(event.x, event.y)
            current_color = canvas.itemcget(item_id, "fill")
            new_color = "white"
            canvas.itemconfig(item_id, fill=new_color)

            col = int(event.x / (sqsize / 30))
            row = int(event.y / (sqsize / 30))

            x_offset = int(sqsize / 30 * col)
            y_offset = int(sqsize / 30 * row)

            if turn == 4:
                new_color = "white"
                turn = 0

            if turn == 3:
                new_color = "green"
                turn = 4

            if turn == 2:
                new_color = "red"
                turn = 3

            if turn == 1:
                new_color = "yellow"
                turn = 2

            if turn == 0:
                new_color = "blue"
                turn = 1

            #canvas.itemconfig(item_id, fill=new_color)
            #if gameboard[row][col] == 0:
            #    gameboard[row][col] = turn

            piece_size = sqsize / 30
            for x, y in piece_rotations[selected_piece][rotate_counter]:
                gameboard[row+y][col+x] = turn
                print(x, y)


            print(row, col)
            for r in gameboard:
                print(r, end=" ")
                print()

            game_progression.append([selected_piece, rotate_counter, new_color, row, col])
            print(game_progression)
            selected_piece = None
            rotate_counter = 0
            draw()
        else:
            return None
        # def update_score(event):
        #    global score_b
        #    score_b += 1
        #    draw()

    def skip_turn(event):
         pass

    def rules_menu(event):
        global rules

        def rules_next(event):
            r_canvas.delete("all")
            r_canvas.create_text(window_sqsize * 9 / window_grid, window_sqsize * 1 / window_grid, text="CORE RULES",
                                 font=("Showcard Gothic", 30))
            r_canvas.create_rectangle(window_sqsize * 1 / window_grid, window_sqsize * 16 / window_grid,
                                      window_sqsize * 4 / window_grid, window_sqsize * 17 / window_grid,
                                      fill="lightblue", activefill="blue", tags="previous")
            r_canvas.create_rectangle(window_sqsize * 14 / window_grid, window_sqsize * 16 / window_grid,
                                      window_sqsize * 17 / window_grid, window_sqsize * 17 / window_grid,
                                      fill="lightblue", activefill="blue", tags="close")
            r_canvas.create_text(window_sqsize * 31 / window_grid / 2, window_sqsize * 35 / window_grid / 2, text="PAGE 2/2", font=("Showcard Gothic", 15))
            r_canvas.create_text(window_sqsize * 5 / window_grid / 2, window_sqsize * 33 / window_grid / 2,
                                 text="PREVIOUS", font=("Showcard Gothic", 15), tags="previous")
            r_canvas.create_text(window_sqsize * 31 / window_grid / 2, window_sqsize * 33 / window_grid / 2,
                                 text="CLOSE", font=("Showcard Gothic", 15), tags="close")
            r_canvas.create_text(window_sqsize * 1 / window_grid, window_sqsize * 4.5 / window_grid,
                                 text="Every player starts on 0 points. The play order starts with blue at the bottom"
                                      " left side of the board. The turns go clockwise continuing with yellow, red and"
                                      " then green before blue goes again. There are the same 21 pieces for every color"
                                      " to play with. You pick a piece and place it on the board accordingly in order"
                                      " to get points. The points consist of the number of individual squares the piece"
                                      " is made of."
                                      "while all the 2-Player-Rules apply.", font=("Showcard Gothic", 12), width=500,
                                 anchor="w")
            r_canvas.create_text(window_sqsize * 9 / window_grid, window_sqsize * 8 / window_grid, text="RULES TO PLACE",
                                 font=("Showcard Gothic", 30))
            r_canvas.create_text(window_sqsize * 1 / window_grid, window_sqsize * 11.5 / window_grid,
                                 text="-- [1st MOVE] -- The piece must cover the corner.\n"
                                      "(Blue -> Bottom left; Yellow -> Upper left; Red -> Upper right; Green -> Bottom right\n"
                                      "-- The piece must be fully placeable on the board\n"
                                      "-- The piece must not overwrite another piece at all\n"
                                      "-- The piece must touch another piece of the same color but only on at least one corner\n"
                                      "-- The piece can touch differently colored pieces freely",
                                 font=("Showcard Gothic", 12), width=500, anchor="w")

        def rules_previous(event):
            r_canvas.delete("all")
            r_canvas.create_text(window_sqsize * 9 / window_grid, window_sqsize * 1 / window_grid, text="CASUAL RULES",
                                 font=("Showcard Gothic", 30))
            r_canvas.create_text(window_sqsize * 1 / window_grid, window_sqsize * 3 / window_grid,
                                 text="Singleplayer Rules: This can only be played against an AI.\n"
                                      "You choose the AI difficulty via Menu beforehand.\n"
                                      "The game is a standartized 2-Player game \n"
                                      "while all the 2-Player-Rules apply.", font=("Showcard Gothic", 12), width=500,
                                 anchor="w")
            r_canvas.create_text(window_sqsize * 1 / window_grid, window_sqsize * 6 / window_grid,
                                 text="2-Players: Every player controls two colors.\n"
                                      "One player controls blue and red while\n the other controls yellow and green.\n"
                                      "Both colors of each player count towards their total points. The playing order remains the same."
                                 , font=("Showcard Gothic", 12), width=500, anchor="w")
            r_canvas.create_rectangle(window_sqsize * 14 / window_grid, window_sqsize * 16 / window_grid,
                                      window_sqsize * 17 / window_grid, window_sqsize * 17 / window_grid,
                                      fill="lightblue", activefill="blue", tags="next")
            r_canvas.create_text(window_sqsize * 31 / window_grid / 2, window_sqsize * 35 / window_grid / 2,
                                 text="PAGE 1/2", font=("Showcard Gothic", 15))
            r_canvas.create_text(window_sqsize * 31 / window_grid / 2, window_sqsize * 33 / window_grid / 2,
                                 text="NEXT", font=("Showcard Gothic", 15), tags="next")
            r_canvas.create_text(window_sqsize * 9 / window_grid, window_sqsize * 8.5 / window_grid, text="KEYBINDS",
                                 font=("Showcard Gothic", 30))
            r_canvas.create_text(window_sqsize * 1 / window_grid, window_sqsize * 10 / window_grid,
                                 text="[LEFT MB] - Hover over a piece and click to select it. Place it on the board via click.",
                                 font=("Showcard Gothic", 12), width=500, anchor="w")
            r_canvas.create_text(window_sqsize * 1 / window_grid, window_sqsize * 11 / window_grid,
                                 text="[R] - Rotate the selected piece by 90° counter-clockwise.",
                                 font=("Showcard Gothic", 12), width=500, anchor="w")
            r_canvas.create_text(window_sqsize * 1 / window_grid, window_sqsize * 12 / window_grid,
                                 text="[E] - Emulate the selected piece in mirrored form.",
                                 font=("Showcard Gothic", 12), width=500, anchor="w")
        def close_menu(event):
            rules.withdraw()

        rules = tk.Tk()
        rules.title("RULES")
        rules.resizable(False, False)
        r_canvas = tk.Canvas(rules, width=600, height=600, bg="lightgreen")
        r_canvas.pack()
        window_sqsize = 600
        window_grid = 18

        r_canvas.create_text(window_sqsize * 9 / window_grid, window_sqsize * 1 / window_grid, text="CASUAL RULES", font=("Showcard Gothic", 30))
        r_canvas.create_text(window_sqsize * 1 / window_grid, window_sqsize * 3 / window_grid, text="Singleplayer Rules: This can only be played against an AI.\n"
                                                                                                    "You choose the AI difficulty via Menu beforehand.\n"
                                                                                                    "The game is a standartized 2-Player game \n"
                                                                                                    "while all the 2-Player-Rules apply.", font=("Showcard Gothic", 12), width=500, anchor="w")
        r_canvas.create_text(window_sqsize * 1 / window_grid, window_sqsize * 6 / window_grid, text="2-Players: Every player controls two colors.\n"
                                                                                                    "One player controls blue and red while\n the other controls yellow and green.\n"
                                                                                                    "Both colors of each player count towards their total points. The playing order remains the same."
                                                                                                    , font=("Showcard Gothic", 12), width=500, anchor="w")
        r_canvas.create_rectangle(window_sqsize * 14 / window_grid, window_sqsize * 16 / window_grid, window_sqsize * 17 / window_grid, window_sqsize * 17 / window_grid, fill="lightblue", activefill="blue", tags="next")
        r_canvas.create_text(window_sqsize * 9 / window_grid, window_sqsize * 8.5 / window_grid, text="KEYBINDS",
                             font=("Showcard Gothic", 30))
        r_canvas.create_text(window_sqsize * 1 / window_grid, window_sqsize * 10 / window_grid, text="[LEFT MB] - Hover over a piece and click to select it. Place it on the board via click.",
                             font=("Showcard Gothic", 12), width=500, anchor="w")
        r_canvas.create_text(window_sqsize * 1 / window_grid, window_sqsize * 11 / window_grid,
                             text="[R] - Rotate the selected piece by 90° counter-clockwise.",
                             font=("Showcard Gothic", 12), width=500, anchor="w")
        r_canvas.create_text(window_sqsize * 1 / window_grid, window_sqsize * 12 / window_grid,
                             text="[E] - Emulate the selected piece in mirrored form.",
                             font=("Showcard Gothic", 12), width=500, anchor="w")
        r_canvas.create_text(window_sqsize * 31 / window_grid / 2, window_sqsize * 35 / window_grid / 2,
                             text="PAGE 1/2", font=("Showcard Gothic", 15))
        r_canvas.create_text(window_sqsize * 31 / window_grid / 2, window_sqsize * 33 / window_grid / 2,
                             text="NEXT", font=("Showcard Gothic", 15), tags="next")
        r_canvas.tag_bind("next", "<Button-1>", rules_next)
        r_canvas.tag_bind("previous", "<Button-1>", rules_previous)
        r_canvas.tag_bind("close", "<Button-1>", close_menu)
        rules.mainloop()

    def take_back(event):
        pass

    def quit(event):
        game.destroy()

    # Calls draw function for the first time
    draw()

    board.tag_bind("board", "<Button-1>", on_place)
    # board.tag_bind("board", "<Button-1>", PosIndex)
    board.tag_bind("skip", "<Button-1>", skip_turn)
    board.tag_bind("rules", "<Button-1>", rules_menu)
    board.tag_bind("take_back", "<Button-1>", take_back)
    board.tag_bind("quit", "<Button-1>", quit)
    # board.bind("<Button-1>", update_score)
    # Every change in the window calls config function
    game.bind("<Configure>", config)
    game.mainloop()


start_button = tk.Button(canvas, text="START GAME", font=("Showcard Gothic", 20), command=main)
start_button.pack(side=tk.BOTTOM, pady=30)

# for item in player_menu.keys():
#    print(item, ": ", player_menu[item])
root.mainloop()
