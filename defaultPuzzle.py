import numpy as np

class defaultPuzzle():
    def __init__(self):
        self.initialState = np.array([[1,2,0],[4,5,3],[7,8,6]])
        
    def printPuzzle(self):
        print("The Puzzle:")
        print(self.initialState[0])
        print(self.initialState[1])
        print(self.initialState[2])