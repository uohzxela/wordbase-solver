# wordbase-solver

Dependencies
* OpenCV and Python bindings 
* [pytesseract](https://github.com/madmaze/pytesseract)

Usage
* `cd wordbase-solver/src`
* `python extract_game_board_text.py wordbase.png` to print out the gameboard in console
* `python tst_wrapper.py` to try out the ternary search tree loaded with dictionary 
* `python solver.py [blue/orange] [/path/to/screenshot.jpg]` to find suitable words in the given screenshot, given the player color

To-do list

1. ~~Extract out gameboard represented by a 2D array of characters~~
2. ~~Implement a dictionary data structure (ternary search tree) with O(w) lookup where w is the length of the word~~
3. ~~Use DFS to find all valid words in 2D array according to the dictionary~~
4. ~~Deploy as web app (AWS EC2)~~

Wordbase Solver is live! http://wordbase.alexjiao.com
