# wordbase-solver

Wordbase Solver is live! http://wordbase.alexjiao.com

##Dependencies
* OpenCV and Python bindings 
* [pytesseract](https://github.com/madmaze/pytesseract) for Optical Character Recognition (OCR)

##Usage
* `cd wordbase-solver/src`
* `python extract_game_board_text.py wordbase.png` to print out the gameboard in console
* `python tst_wrapper.py` to try out the tree loaded with dictionary 
* `python solver.py [blue/orange] [/path/to/screenshot.jpg]` to find suitable words in the given screenshot, given the player color

##How it works
* The screenshot is preprocessed using OpenCV functions to generate a B&W image which makes OCR more effective
    * Simple thresholding is used to convert the screenshot to B&W
    * Contour finding is used to find inverted regions and invert them
    * Erosion is used to deal with tricky cases where two diagonal inverted regions stick with each other, making it difficult to obtain the contours
* Tesseract is used to recognize individual characters from the intermediate B&W image
* Characters are stored in a 2D array, along with its color mapping.
* A tree data structure is initialized to store 170k+ English words from the dictionary with O(w) lookup where w is the length of the word
* A graph of characters and their neighbors is created from the 2D array, and DFS is employed to find all valid words from the graph
* The list of valid words is sorted according to the word's promixity to the opponent's base (the nearer, the better).

##To-do list
1. Dockerization since setting up dependencies is quite time consuming
2. Make web app more user-friendly


