from tkinter import *
from random import *

class tetris():                 #defines the tetris shape
    SHAPES = ([(0, 0), (1, 0), (0, 1), (1, 1)],     # square
              [(0, 0), (1, 0), (2, 0), (3, 0)],     # line
              [(2, 0), (0, 1), (1, 1), (2, 1)],     # right el
              [(0, 0), (0, 1), (1, 1), (2, 1)],     # left el
              [(0, 1), (1, 1), (1, 0), (2, 0)],     # right wedge
              [(0, 0), (1, 0), (1, 1), (2, 1)],     # left wedge
              [(1, 0), (0, 1), (1, 1), (2, 1)])     # symmetrical wedge

    tetris_grid_size = 20  # defines the tetris shape

    win_width = 300
    GAME_HEIGHT = 500
    Box_Entry_Point = win_width / 2 / tetris_grid_size * tetris_grid_size - tetris_grid_size    #defing the entry point for the first item

    def __init__(self):
        self._level = 1
        self._score = 0
        self.countblocks = 0
        self.speed = 500

        self.root = Tk()
        self.root.geometry("500x550") 
        self.root.configure(bg = "grey")
        self.root.title('Tetris')
        # Arrow keys binding
        self.root.bind("<KeyRelease-Up>", self.upArrow)
        self.root.bind("<KeyRelease-Down>", self.downArrow)
        self.root.bind("<KeyRelease-Left>", self.leftArrow)
        self.root.bind("<KeyRelease-Right>", self.rightArrow)
        self.game_window()
        self.label_for_level()
        self.window_for_nextpiece()
    

    def upArrow(self, event):   # calling the function for any event button pressed.
        self.current_shape.rotate()
    

    def downArrow(self, event):
        self.tetris_to_floor()
    

    def leftArrow(self, event):
        self.current_shape.move((-1, 0))
    

    def rightArrow(self, event):
        self.current_shape.move((1, 0))


    def new_game(self): #defining how a new game should be started
        self.level = 1
        self.score = 0
        self.blockcount = 0
        self.speed = 500

        self.canvas.delete("all")
        self.next_canvas.delete("all")

        self.main_game_frame()
        self.window_for_nxt_item()

        self.current_shape = None
        self.next_piece = None        

        self.game_board = [[0] * ((tetris.win_width - 20) // tetris.tetris_grid_size)\
                           for _ in range(tetris.GAME_HEIGHT // tetris.tetris_grid_size)]

        self.update_piece()

    def update_piece(self):
        if not self.next_piece:
            self.next_piece = Blocks(self.next_canvas, (20,20))

        self.current_shape = Blocks(self.canvas, (tetris.Box_Entry_Point, 0), self.next_piece.shape)
        self.next_canvas.delete("all")
        self.window_for_nxt_item()
        self.next_piece = Blocks(self.next_canvas, (20,20))

    def start(self):
        self.new_game()
        self.root.after(self.speed, None)
        self.tetris_to_fall()
        self.root.mainloop()

    def tetris_to_fall(self):
        if not self.current_shape.move((0,1)):
            self.completed_row()
            self.game_board = self.canvas.game_board()
            self.update_piece()

            if self.game_is_over():
                return
            else:
                self.countblocks += 1
                self.score += 0

        self.root.after(self.speed, self.tetris_to_fall)

    def tetris_to_floor(self):
        self.current_shape.move(self.current_shape.predict_movement(self.game_board))


    def game_status_updates(self):
        self.status_var.set(f"Level:{self.level},Score:{self.score}")
        self.status.update()

    def game_is_over(self): # check if there is space for the new shape to fall and if no space then the game is over.
        if not self.current_shape.move((0,1)):

            self.try_again_button = Button(self.root,bg="black",fg="white", text="Try Again", command=self.try_again)
            self.exit_button = Button(self.root,bg="red",fg="white",text="Exit", command=self.exit) 
            self.try_again_button.place(x = tetris.win_width + 30, y = 250, width=150, height=40)
            self.exit_button.place(x = tetris.win_width + 30, y = 350, width=150, height=40)
            return True
        return False

    def try_again(self):
        self.try_again_button.destroy()
        self.exit_button.destroy()
        self.start()

    def exit(self):
        self.root.quit()     

    def completed_row(self):
        y_coords = [self.canvas.coords(box)[3] for box in self.current_shape.boxes]
        complete_row = self.canvas.completed_row(y_coords)
        if complete_row == 1:
            self.score += 10
        elif complete_row == 2:
            self.score += 25
        elif complete_row == 3:
            self.score += 50
        elif complete_row >= 4:
            self.score += 100

    def game_window(self):
        self.canvas = gamesetup(self.root, 
                             width = tetris.win_width, 
                             height = tetris.GAME_HEIGHT)
        self.canvas.pack(padx=5 , pady=10, side=LEFT)

    def main_game_frame(self):
        self.canvas.create_rectangle(10, 20, self.win_width-10, self.GAME_HEIGHT, tags="frame")
        self.canvas['background']='#AEE8F5'
        starting_position_row = 10
        starting_position_col = self.tetris_grid_size

        for i in range(0, 13):
            self.canvas.create_line(starting_position_row + self.tetris_grid_size, 0 + self.tetris_grid_size, starting_position_row + self.tetris_grid_size, self.GAME_HEIGHT, fill="red")
            starting_position_row = starting_position_row + self.tetris_grid_size
        
        for i in range(0, 23):
            self.canvas.create_line(10, starting_position_col + self.tetris_grid_size, self.win_width-10, starting_position_col + self.tetris_grid_size, fill="red")
            starting_position_col = starting_position_col + self.tetris_grid_size

    def label_for_level(self):
        self.status_var = StringVar()        
        self.status = Label(self.root, 
                            textvariable=self.status_var, bg="black", fg="white",
                            font=("Helvetica", 10, "bold"))
        self.status.pack()

    def window_for_nextpiece(self): #setting side window for the next item 
        self.next_canvas = Canvas(self.root,
                                 width = 105,
                                 height = 105)
        self.next_canvas.pack(padx=5, pady=10)
        self.next_canvas.configure(bg = "grey")
        self.next_piece_text = StringVar()
        self.next_piece_label = Label(self.root,
                                textvariable=self.next_piece_text,bg="pink",
                                font=("Helvetica", 10, "bold"))
        self.next_piece_label.pack(padx=10, pady=10)
        self.next_piece_text.set("Next Piece")

    def window_for_nxt_item(self):
        self.next_canvas.create_rectangle(10, 10, 105, 105, tags="frame")
        self.next_canvas["background"]="#ffffed"

        #accessing the property we assigned.
    def get_game_level(self): 
        return self._level

    def set_game_level(self, level):
        self.speed = 500 - (level - 1) * 25
        self._level = level
        self.game_status_updates()

    def get_game_score(self):
        return self._score

    def set_game_score(self, score):
        self._score = score
        self.game_status_updates()

    def get_game_blockcount(self):
        return self.countblocks

    def set_game_blockcount(self, blockcount):
        self.level = blockcount // 5 + 1
        self.countblocks = blockcount

    level = property(get_game_level, set_game_level)
    score = property(get_game_score, set_game_score)
    blockcount = property(get_game_blockcount, set_game_blockcount)

class gamesetup(Canvas):
    def completed_row(self, coordinates_y):
        cleaned_lines = 0
        coordinates_y = sorted(coordinates_y)
        for y in coordinates_y:
            if sum(1 for box in self.find_withtag('game') if self.coords(box)[3] == y) == \
               ((tetris.win_width - 20) // tetris.tetris_grid_size):
                self.remove_row([box
                                for box in self.find_withtag('game')
                                if self.coords(box)[3] == y])

                self.move_box([box
                                 for box in self.find_withtag('game')
                                 if self.coords(box)[3] < y])
                cleaned_lines += 1
        return cleaned_lines

    def remove_row(self, clear_boxes):
        for box in clear_boxes:
            self.delete(box)
        self.update()

    def move_box(self, drop_boxes):
        for box in drop_boxes:
            self.move(box, 0, tetris.tetris_grid_size)
        self.update()

    def game_board(self):
        board = [[0] * ((tetris.win_width - 20) // tetris.tetris_grid_size)\
                 for _ in range(tetris.GAME_HEIGHT // tetris.tetris_grid_size)]
        for box in self.find_withtag('game'):
            x, y, _, _ = self.coords(box)
            board[int(y // tetris.tetris_grid_size)][int(x // tetris.tetris_grid_size)] = 1
        return board

class Shape():
    def __init__(self, cordins = None):
        if not cordins:
            self.cordinates = choice(tetris.SHAPES)
        else:
            self.cordinates = cordins

    def rotations(self):    #definingg the rotation of the tetris setting
        max_x = max(self.cordinates, key=lambda x:x[0])[0]
        new_original = (max_x, 0)

        rotate = [(new_original[0] - coord[1],
                    new_original[1] + coord[0]) for coord in self.cordinates]

        min_x = min(rotate, key=lambda x:x[0])[0]
        min_y = min(rotate, key=lambda x:x[1])[1]
        return [(coord[0] - min_x, coord[1] - min_y) for coord in rotate]

    @property
    def coords(self):
        return self.cordinates

    def rotate_directions(self):
        rotated = self.rotations()
        directions = [(rotated[i][0] - self.cordinates[i][0],
                       rotated[i][1] - self.cordinates[i][1]) for i in range(len(self.cordinates))]

        return directions

    def rotate(self):  
        self.cordinates = self.rotations()

    @property
    def matrix(self):
        return [[1 if (j, i) in self.cordinates else 0 \
                 for j in range(max(self.cordinates, key=lambda x: x[0])[0] + 1)] \
                 for i in range(max(self.cordinates, key=lambda x: x[1])[1] + 1)]

    def fall(self, board, offset):
        off_x, off_y = offset
        last_level = len(board) - len(self.matrix) + 1
        for level in range(off_y, last_level):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    if board[level+i][off_x+j] == 1 and self.matrix[i][j] == 1:
                        return level - 1
        return last_level - 1  


class Blocks():
    def __init__(self, canvas, start_point, shape = None):
        self.shapes = shape
        if not shape:
            self.shapes = Shape()
        self.canvas = canvas
        self.boxes = self.create_tetris_boxes(start_point)

    @property
    def shape(self):
        return self.shapes

    def move(self, direction):
        if all(self.can_move_shape(self.canvas.coords(box), direction) for box in self.boxes):
            x, y = direction
            for box in self.boxes:
                self.canvas.move(box,
                                 x * tetris.tetris_grid_size,
                                 y * tetris.tetris_grid_size)
            return True
        return False

    def rotate(self):
        directions = self.shapes.rotate_directions()
        if all(self.can_move_shape(self.canvas.coords(self.boxes[i]), directions[i]) for i in range(len(self.boxes))):
            self.shapes.rotate()
            for i in range(len(self.boxes)):
                x, y = directions[i]
                self.canvas.move(self.boxes[i],
                                 x * tetris.tetris_grid_size,
                                 y * tetris.tetris_grid_size)

    @property
    def offset(self):
        return (min(int(self.canvas.coords(box)[0]) // tetris.tetris_grid_size for box in self.boxes),
                min(int(self.canvas.coords(box)[1]) // tetris.tetris_grid_size for box in self.boxes))

    def predict_drop(self, board):
        level = self.shapes.fall(board, self.offset)
        self.remove_predicts()

        min_y = min([self.canvas.coords(box)[1] for box in self.boxes])
        for box in self.boxes:
            x1, y1, x2, y2 = self.canvas.coords(box)
            box = self.canvas.create_rectangle(x1,
                                               level * tetris.tetris_grid_size + (y1 - min_y),
                                               x2,
                                               (level + 1) * tetris.tetris_grid_size + (y1 - min_y),
                                               fill="yellow",
                                               tags = "predict")

    def predict_movement(self, board):
        level = self.shapes.fall(board, self.offset)
        min_y = min([self.canvas.coords(box)[1] for box in self.boxes])
        return (0, level - (min_y // tetris.tetris_grid_size))

    def create_tetris_boxes(self, start_point):
        boxes = []
        off_x, off_y = start_point
        for coord in self.shapes.coords:
            x, y = coord
            box = self.canvas.create_rectangle(x * tetris.tetris_grid_size + off_x,
                                               y * tetris.tetris_grid_size + off_y,
                                               x * tetris.tetris_grid_size + tetris.tetris_grid_size + off_x,
                                               y * tetris.tetris_grid_size + tetris.tetris_grid_size + off_y,
                                               fill="green",
                                               tags="game")
            boxes += [box]

        return boxes

    def can_move_shape(self, box_coords, new_pos):  #check if the shape can move
        x, y = new_pos
        x = x * tetris.tetris_grid_size
        y = y * tetris.tetris_grid_size
        x_left, y_up, x_right, y_down = box_coords
            ## checks if the moving box will overlap another box
        overlap = set(self.canvas.find_overlapping((x_left + x_right) / 2 + x, 
                                                   (y_up + y_down) / 2 + y, 
                                                   (x_left + x_right) / 2 + x,
                                                   (y_up + y_down) / 2 + y))
        other_items = set(self.canvas.find_withtag('game')) - set(self.boxes)

        if y_down + y > tetris.GAME_HEIGHT or \
           x_left + x < 0 or \
           x_right + x > tetris.win_width or \
           overlap & other_items:
            return False
        return True        



if __name__ == '__main__':
    game = tetris()
    game.start()
