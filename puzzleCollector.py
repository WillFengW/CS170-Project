import numpy as np
import re
from defaultPuzzle import defaultPuzzle

class puzzleCollector(defaultPuzzle):
    def __init__(self):
        super().__init__()
        
    def setPuzzle(self):
        print("Enter your puzzle, use a zero to represent the blank")
        row = input("Enter the first row, use space or tabs between numbers: ")
        self.initialState[0] = [int(i) for i in re.findall(r'\b\d+\b', row)]
        row = input("Enter the second row, use space or tabs between numbers: ")
        self.initialState[1] = [int(i) for i in re.findall(r'\b\d+\b', row)]
        row = input("Enter the third row, use space or tabs between numbers: ")
        self.initialState[2] = [int(i) for i in re.findall(r'\b\d+\b', row)]
        
    #def checkPuzzle(self):
    #   check if the puzzle is valid
        
        