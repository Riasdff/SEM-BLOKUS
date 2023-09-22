import tkinter as tk
from tkinter import *
from const import *
from blocks import *
from gameprog import *

pieces = {"one": [(0, 0)],
          "two": [(0, 0), (0, 1)],
          "three_i": [(0, 0), (1, 0), (-1, 0)],
          "three_l": [(0, 0), (0, 1), (1, 1)],
          "four_i": [(0, 0), (1, 0), (2, 0), (-1, 0)],
          "four_l": [(0, 0), (0, -1), (0, 1), (1, 1)],
          "four_s": [(0, 0), (-1, 0), (0, -1), (-1, -1)],
          "four_o": [(0, 0), (0, -1), (1, 1), (1, -1)],
          "four_t": [(0, 0), (0, 1), (-1, 0), (1, 0)],
          "five_f": [(0, 0), (-1, 0), (0, -1), (1, -1), (0, 1)],
          "five_i": [(0, 0), (-1, 0), (-2, 0), (1, 0), (2, 0)],
          "five_l": [(0, 0), (0, 1), (0, -1), (0, -2), (1, 1)],
          "five_n": [(0, 0), (0, 1), (0, 2), (1, 0), (1, -1)],
          "five_p": [(0, 0), (0, 1), (0, -1), (1, -1), (1, 0)],
          "five_t": [(0, 0), (0, 1), (0, 2), (-1, 0), (1, 0)],
          "five_u": [(0, 0), (-1, 0), (-1, -1), (1, 0), (1, -1)],
          "five_v": [(0, 0), (-1, 0), (-2, 0), (0, -1), (0, -2)],
          "five_w": [(0, 0), (0, 1), (-1, 1), (1, -1), (1, 0)],
          "five_x": [(0, 0), (-1, 0), (0, -1), (1, 0), (0, 1)],
          "five_y": [(0, 0), (-1, 0), (0, -1), (0, 1), (0, 2)],
          "five_z": [(0, 0), (0, -1), (-1, -1), (1, 1), (0, 1)]
          }

gameboard = [[0 for row in range(rows)] for column in range(columns)]
print(gameboard)

class Shape:
    def __init__(self, name, color, squares):
        self.name = name
        self.color = color
        self.squares = squares
        self.is_clicked = False

        self.shape_width = shape_width
        self.shape_height = shape_height
        self.offset_x = offset_x
        self.offset_y = offset_y

    def draw(self):
        pass

    def clicked(self):
        pass

    def get_info(self):
        pass

    def place(self):
        pass

shape1 = Shape(one, "blue", 1)
shape2 = Shape(two, "blue", 2)
shape3 = Shape(three_i, "blue", 3)
shape4 = Shape(three_l, "blue", 3)
shape5 = Shape(four_i, "blue", 4)
shape6 = Shape(four_l, "blue", 4)
shape7 = Shape(four_s, "blue", 4)
shape8 = Shape(four_o, "blue", 4)
shape9 = Shape(four_t, "blue", 4)
shape10 = Shape(five_f, "blue", 5)
shape11 = Shape(five_i, "blue", 5)
shape12 = Shape(five_l, "blue", 5)
shape13 = Shape(five_n, "blue", 5)
shape14 = Shape(five_p, "blue", 5)
shape15 = Shape(five_t, "blue", 5)
shape16 = Shape(five_u, "blue", 5)
shape17 = Shape(five_v, "blue", 5)
shape18 = Shape(five_w, "blue", 5)
shape19 = Shape(five_x, "blue", 5)
shape20 = Shape(five_y, "blue", 5)
shape21 = Shape(five_z, "blue", 5)

game = tk.Tk()
game.title("Blokus")
game.geometry("800x800")
game.minsize(width=600, height=600)

canvas = tk.Canvas(game, width=default_width, height=default_height, bg="gray80")
canvas.pack(fill=BOTH, expand=TRUE)

minsize = 0
if game.winfo_width() < game.winfo_height():
    minsize = game.winfo_height()
else:
    minsize = game.winfo_width()

def draw_board(rows, columns):
    for row in range(rows):
        for column in range(columns):
            canvas.create_rectangle(column * shape_width, row * shape_height,
                                    column * shape_width + shape_width, row * shape_height + shape_height,
                                    fill="white", tags="board")


def config(event=None):
    canvas.delete("all")
    draw_board(rows, columns)


def highlight(event):
    canvas.itemconfig("board", activefill="lightblue")


def outlight(event):
    canvas.itemconfig("board", activefill="lightblue")


def draw(event):
    global turn
    canvas = event.widget
    item_id = canvas.find_closest(event.x, event.y)
    current_color = canvas.itemcget(item_id, "fill")
    new_color = "white"
    if turn == 4:
        new_color = "white"
        turn = 0
        
    if turn == 3:
        new_color = "green"

    if turn == 2:
        new_color = "red"

    if turn == 1:
        new_color = "yellow"

    if turn == 0:
        new_color = "blue"

    turn += 1

    canvas.itemconfig(item_id, fill=new_color)

    row = int(event.y / shape_width)
    column = int(event.x / shape_height)

    gameboard[row][column] = 1
    print(row, column)
    #print(gameboard)

    game_progression.append(f"{new_color}: {row} {column}")
    print(game_progression)

def take_back():
    global turn
    turn -= 1


draw_board(rows, columns)

canvas.tag_bind("board", "<Enter>", highlight)
canvas.tag_bind("board", "<Leave>", outlight)
canvas.tag_bind("board", "<Button-1>", draw)
canvas.bind("<Configure>", config)

game.mainloop()
