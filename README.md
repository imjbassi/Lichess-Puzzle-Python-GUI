# Lichess Puzzle GUI in Python

<sup>This was a project I worked on entirely on my Mac, getting libraries and everything to work to prove I can work Python on this machine was the main goal.</sup>

The Chess Puzzle App is a simple interactive application built using Python and the Tkinter library allowing you to look at different puzzles in the Lichess puzzle databse.


## Introduction
This Python program loads chess puzzles from a CSV file, displays them on a graphical chessboard using tkinter, and enables users to navigate through moves using "Next" and "Previous" buttons. It's a handy tool for practicing and improving chess tactics.

## Features
- Loads chess puzzles from a CSV file.
- Displays puzzles on a graphical chessboard using tkinter.
- Allows users to navigate through moves using "Next" and "Previous" buttons.
- Picks a random puzzle each time the program starts.
- Shows the chessboard position corresponding to the current move.
- Handles both white and black moves.
- Displays puzzle FEN (Forsyth-Edwards Notation) in the terminal.
- Provides an interactive way to practice and improve chess tactics.

## Installation
1. Clone this repository to your local machine using: `git clone https://github.com/yourusername/Lichess-Puzzle-Python-GUI
.git`
2. Install required dependencies/libraries:
- Libraries: `pip install -r requirements.txt`
- Download https://database.lichess.org/#puzzles and `brew install zstd` then use `zstd -d yourfilename.zst` to get a CSV
  - Puzzles are formatted as standard CSV. The fields are as follows: PuzzleId,FEN,Moves,Rating,RatingDeviation,Popularity,NbPlays,Themes,GameUrl,OpeningTags


## Usage
<img src="https://raw.githubusercontent.com/imjbassi/Lichess-Puzzle-Python-GUI/main/Images/GUI%20Screenshot.png" width="300">

1. Run the app using Python: `python chess_puzzle_app.py`
2. Make sure the file path for the CSV is set after extracting from the Lichess puzzle database
   
   - <img src="https://raw.githubusercontent.com/imjbassi/Lichess-Puzzle-Python-GUI/main/Images/LichessPuzzleDB.png" width="400">
3. You can use the next or previous buttons to see the moves in the puzzle as it's in the correct orientation, the FEN will also be printed in the console.

- <img src="https://raw.githubusercontent.com/imjbassi/Lichess-Puzzle-Python-GUI/main/Images/Terminal%20Example.png" width="400">


## Code
<img src="https://raw.githubusercontent.com/imjbassi/Lichess-Puzzle-Python-GUI/main/Images/ChessPY.png" width="500">

## Potential Mac Problems
If it seems like the cairocffi library try installing cairocffi and its required system libraries by running
- `brew install cairo`
- `sudo apt-get install libcairo2-dev`
- `conda install -c conda-forge cairocffi` (ultimately worked for me)
- `brew install web-browser`
- `brew install --cask edfbrowser`
- `pip install Pillow-SVG`

If you get "ImportError: Missing optional dependency 'zstandard' use `pip install zstandard`

"zsh: permission denied: lichess_db_puzzle.csv"  use `chmod +x lichess_db_puzzle.csv`

## Documenting my Windows Problems

It seems like you're encountering an issue with the cairosvg library and its dependency on the Cairo graphics library. The error message suggests that the "cairo-2" library or its variants cannot be found, which means the Cairo library is missing or not properly installed on your system.

To resolve this issue, you'll need to install the Cairo graphics library. Here's how you can do it:

Windows:
You can try installing the required libraries using pre-built binary packages. You can download the required files from the GTK for Windows Runtime Environment Installer:[ https://www.gtk.org/download/windows.php](https://www.gtk.org/docs/installations/windows/#using-gtk-from-msys2-packages)
After installing GTK, make sure to add its bin directory to your system's PATH environment variable.
