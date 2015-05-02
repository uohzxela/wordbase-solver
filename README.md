# wordbase-solver

Dependencies
* OpenCV and Python bindings 
* [pytesseract](https://github.com/madmaze/pytesseract)
* Boost

Usage
* `cd wordbase-solver/src`
* `python extract_game_board_text.py wordbase.png` to print out the gameboard in console

To-do list

1. ~~Extract out gameboard represented by a 2D array of characters~~
2. ~~Implement a dictionary data structure (ternary search tree) with O(w) lookup where w is the length of the word~~
3. Implement Python bindings to access ternary search tree coded in C++ from Python
3. Use DFS to find all valid words in 2D array according to the dictionary
