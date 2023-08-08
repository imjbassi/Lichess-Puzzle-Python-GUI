# Lichess-Puzzle-Python-GUI
The Chess Puzzle App is a simple interactive application built using Python and the Tkinter library. It allows users to solve chess puzzles by providing the correct sequence of moves for a given puzzle position. The app loads puzzle data from a CSV file and displays the chessboard along with the puzzle information. Users can input their moves and receive feedback on whether their moves are correct or not. The app also provides navigation buttons to move through the puzzle's moves step by step.
- This was a project I worked on entirely on my Mac, getting libraries and everything to work to prove I can work Python on this machine was the main goal.

## Features
- Load chess puzzles from a CSV file.
- Display chessboard positions and puzzle information.
- Allow users to input moves and check their correctness.
- Provide navigation buttons to move through the puzzle's moves.
- User-friendly graphical interface using Tkinter.
- Supports puzzles with FEN positions and UCI move sequences.

## Prerequisites
- Python3
- Tkinter
- Lichess CSV Library https://database.lichess.org/#puzzles

- brew install zstd then use zstd -d yourfilename.zst to get a CSV

## Installation
1. Clone this repository to your local machine using: `git clone https://github.com/yourusername/Lichess-Puzzle-Python-GUI
.git`
2. Navigate to the project directory: `cd Lichess-Puzzle-Python-GUI`
3. Run the app using Python: `python chess_puzzle_app.py`

## Usage
- Launch the app by running chess_puzzle_app.py.
- The app will load a random puzzle from the provided CSV file and display the initial position on the chessboard.
- Follow the displayed puzzle information, make your move in the input field, and click the "Check Move" button.
- If your move is correct, the app will display "Correct move!"; otherwise, it will show the correct move(s).
- Use the "Next Move" and "Previous Move" buttons to navigate through the puzzle's moves.
- Use the "Next Puzzle" button to load a new puzzle.

## Sample CSV Format
The CSV file should contain puzzle data in the following format: 
`FEN,Moves
fen_of_initial_position,uci_move_sequence
fen_of_another_position,uci_move_sequence
...`

## Acknowledgments
This app was developed as part of a learning project and is not intended for commercial use.
The puzzles used in this app are for educational purposes and were obtained from public chess puzzle datasets.

## License
This project is licensed under the MIT License.

## Extra
Libraries I went through this project:

pip install pandas
pip install python-chess
pip install python-lichess
pip install cairosvg chess python-chess pillow
pip install cairosvg

- It seemed like the cairocffi library was missing so I tried installing cairocffi and its required system libraries by running:

brew install cairo
sudo apt-get install libcairo2-dev
conda install -c conda-forge cairocffi (ultimately worked for me)
brew install webbrowser
brew install --cask edfbrowser
pip install Pillow-SVG
