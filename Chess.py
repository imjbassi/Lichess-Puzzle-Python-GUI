import pandas as pd
import random
import tkinter as tk
from PIL import Image, ImageTk
import chess
import chess.svg
from cairosvg import svg2png

def load_puzzles_from_csv(csv_file):
    df = pd.read_csv(csv_file)
    return df

def preprocess_uci_move(uci_move):
    return ''.join(filter(str.isalnum, uci_move))

def pick_random_puzzle(df):
    random_index = random.randint(0, len(df) - 1)
    return df.iloc[random_index]

def convert_uci_to_san(board, uci_move):
    try:
        move = chess.Move.from_uci(uci_move)
        if move in board.legal_moves:
            san_move = board.san(move)
            return san_move
    except ValueError:
        pass
    return ""

def display_chessboard(fen, uci_moves, canvas):
    board = chess.Board(fen)
    
    if not board.turn:
        board = board.mirror()
    
    for uci_move in uci_moves:
        move = chess.Move.from_uci(uci_move)
        if move in board.legal_moves:
            board.push(move)

    svg_data = chess.svg.board(board=board, size=250)
    png_data = svg2png(bytestring=svg_data.encode('utf-8'))

    tk_img = ImageTk.PhotoImage(data=png_data)
    canvas.create_image(0, 0, anchor=tk.NW, image=tk_img)
    canvas.image = tk_img

class ChessPuzzleApp:
    def __init__(self, csv_file):
        self.puzzle_data = load_puzzles_from_csv(csv_file)
        self.root = tk.Tk()
        self.root.title("Chess Puzzle")
        self.root.geometry("400x600")

        self.canvas = tk.Canvas(self.root, width=300, height=300)
        self.canvas.pack()

        self.user_input = tk.StringVar()
        self.entry = tk.Entry(self.root, textvariable=self.user_input)
        self.entry.pack()

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

        self.fen_label = tk.Label(self.root, text="")
        self.fen_label.pack()

        self.turn_label = tk.Label(self.root, text="")
        self.turn_label.pack()

        self.next_button = tk.Button(self.root, text="Next Move", command=self.load_next_move, state=tk.DISABLED)
        self.next_button.pack()

        self.prev_button = tk.Button(self.root, text="Previous Move", command=self.load_prev_move, state=tk.DISABLED)
        self.prev_button.pack()

        self.next_puzzle_button = tk.Button(self.root, text="Next Puzzle", command=self.load_next_puzzle)
        self.next_puzzle_button.pack()

        self.load_next_puzzle()
        self.root.mainloop()

    def update_moves(self):
        board = chess.Board(self.fen)
        if board.turn:
            self.turn_label.config(text="White to move")
        else:
            self.turn_label.config(text="Black to move")
            board = board.mirror()
        display_chessboard(board.fen(), self.uci_moves[:self.move_index], self.canvas)

        self.next_button.config(state=tk.NORMAL)
        self.prev_button.config(state=tk.NORMAL)
        
        if self.move_index >= len(self.uci_moves):
            self.next_button.config(state=tk.DISABLED)
        if self.move_index <= 0:
            self.prev_button.config(state=tk.DISABLED)

    def load_next_puzzle(self):
        self.puzzle = pick_random_puzzle(self.puzzle_data)
        self.fen = self.puzzle.get('FEN', "")
        self.uci_moves = [preprocess_uci_move(move) for move in self.puzzle.get('Moves', "").split()]
        self.san_moves = [convert_uci_to_san(chess.Board(self.fen), uci_move) for uci_move in self.uci_moves if
                        convert_uci_to_san(chess.Board(self.fen), uci_move)]
        self.move_index = 0
        
        self.fen_label.config(text=f"FEN: {self.fen}")
        self.update_moves()
        
        self.next_button.config(state=tk.NORMAL)
        self.prev_button.config(state=tk.DISABLED)

    def check_move(self):
        user_move = self.user_input.get()
        if user_move in self.san_moves:
            self.result_label.config(text="Correct move!")
        else:
            self.result_label.config(text=f"Incorrect move. The correct move(s) is/are: {', '.join(self.san_moves)}")
    
    def load_next_move(self):
        if self.move_index < len(self.uci_moves) - 1:
            self.move_index += 1
            self.update_moves()
            self.prev_button.config(state=tk.NORMAL)
        if self.move_index == len(self.uci_moves) - 1:
            self.next_button.config(state=tk.DISABLED)

    def load_prev_move(self):
        if self.move_index > 0:
            self.move_index -= 1
            self.update_moves()
            self.next_button.config(state=tk.NORMAL)
        if self.move_index == 0:
            self.prev_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    csv_file = "lichess_db_puzzle.csv"
    app = ChessPuzzleApp(csv_file)