# wordbase-solver

OpenCV used for image processing
* Simple threshold
* Finding contours

Tesseract used for optical character recognition
* pytesseract library

Usage
* `cd wordbase-solver/src`
* `python extract_game_board_text.py wordbase.png` to print out the gameboard in console

To-do list

1. ~~Extract out gameboard represented by a 2D array of characters~~
2. Implement a dictionary data structure with O(w) lookup where w is the length of the word
  * Tries? Sorted sets? 
3. Use DFS to find all valid words in 2D array according to the dictionary
