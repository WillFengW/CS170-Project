import numpy as np


class savedState():
    def __init__(self, puzzle=np.zeros((3, 3))):
        self.currentState = np.copy(puzzle)
        self.usedOperator = []
        self.expandedOperator = ""
        self.Gn = 0
        self.Hn = 0

    def returnPuzzle(self):
        return self.currentState

    def puzzleInitializer(self, puzzle: np.ndarray):
        self.currentState = np.copy(puzzle)

    def comparePuzzle(self, left: np.ndarray, right: np.ndarray):
        if (np.array_equal(left, right)): return True

    def printCurrState(self):
        print("Current puzzle: ")
        print(self.currentState[0])
        print(self.currentState[1])
        print(self.currentState[2])

    def printCurrOperator(self):
        print("You should not go " + self.expandedOperator + " now")

    def printGH(self):
        print("g(n) = ", self.Gn)
        print("h(n) = ", self.Hn)

    def printAll(self):
        self.printCurrState()
        self.printCurrOperator()
        self.printGH()