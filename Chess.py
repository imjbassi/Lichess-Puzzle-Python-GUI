import pandas as pd
import random
import tkinter as tk
from PIL import Image, ImageTk
import chess
import chess.svg
from cairosvg import svg2png

# Function to load puzzle data from a CSV file
def load_puzzles_from_csv(csv_file):
    df = pd.read_csv(csv_file)
    return df

# Function to preprocess a UCI move
def preprocess_uci_move(uci_move):
    return ''.join(filter(str.isalnum, uci_move))

# Function to pick a random puzzle from the puzzle data
def pick_random_puzzle(df):
    random_index = random.randint(0, len(df) - 1)
    return df.iloc[random_index]

# Function to display the chessboard
def display_chessboard(fen, canvas):
    board = chess.Board(fen)
    svg_data = chess.svg.board(board=board, size=250)
    png_data = svg2png(bytestring=svg_data.encode('utf-8'))

    tk_img = ImageTk.PhotoImage(data=png_data)
    canvas.create_image(0, 0, anchor=tk.NW, image=tk_img)
    canvas.image = tk_img

# Chess Puzzle App class
class ChessPuzzleApp:
    def __init__(self, csv_file):
        self.puzzle_data = load_puzzles_from_csv(csv_file)
        self.root = tk.Tk()
        self.root.title("Chess Puzzle")
        self.root.geometry("400x600")

        self.board = chess.Board()
        self.move_index = 0

        self.canvas = tk.Canvas(self.root, width=300, height=300)
        self.canvas.pack()

        # Next Move button
        self.next_button = tk.Button(self.root, text="Next Move", command=self.load_next_move, state=tk.DISABLED)
        self.next_button.pack()

        # Previous Move button
        self.prev_button = tk.Button(self.root, text="Previous Move", command=self.load_prev_move, state=tk.DISABLED)
        self.prev_button.pack()

        # Next Puzzle button
        self.next_puzzle_button = tk.Button(self.root, text="Next Puzzle", command=self.load_next_puzzle)
        self.next_puzzle_button.pack()

        # Load the first puzzle
        self.load_next_puzzle()
        self.root.mainloop()

    # Function to update the displayed moves and chessboard
    def update_moves(self):
        to_play_color = "black" if self.fen.split()[1] == 'w' else "white"
        self.display_current_board(to_play_color)

        if self.move_index >= len(self.uci_moves) - 1:
            self.next_button.config(state=tk.DISABLED)
        else:
            self.next_button.config(state=tk.NORMAL)

        if self.move_index <= 0:
            self.prev_button.config(state=tk.DISABLED)
        else:
            self.prev_button.config(state=tk.NORMAL)

    # Function to display the current board state
    def display_current_board(self, to_play_color):
        board = chess.Board(self.fen)
        for uci_move in self.uci_moves[:self.move_index + 1]:
            move = chess.Move.from_uci(uci_move)
            if move in board.legal_moves:
                board.push(move)
        display_chessboard(board.fen(), self.canvas)

    # Function to load the next puzzle
    def load_next_puzzle(self):
        self.puzzle = pick_random_puzzle(self.puzzle_data)
        self.fen = self.puzzle.get('FEN', "")
        self.uci_moves = [preprocess_uci_move(move) for move in self.puzzle.get('Moves', "").split()]

        self.move_index = 0
        self.next_button.config(state=tk.NORMAL)
        self.prev_button.config(state=tk.DISABLED)

        # Update the board's state after updating puzzle data
        self.update_moves()

        # Print the FEN in the terminal
        print("Current FEN:", self.fen)

    # Function to load the next move
    def load_next_move(self):
        self.move_index += 1
        self.update_moves()

    # Function to load the previous move
    def load_prev_move(self):
        self.move_index -= 1
        self.update_moves()

# Entry point of the program
if __name__ == "__main__":
    csv_file = "/Users/jaiveerbassi/Downloads/lichess_db_puzzle.csv"  # Change this to the path of your CSV file
    app = ChessPuzzleApp(csv_file)