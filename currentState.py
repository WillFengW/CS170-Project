from defaultPuzzle import defaultPuzzle
import numpy as np

class currentState():
    def __init__(self, dp: defaultPuzzle):
        self.currentState = np.copy(dp.expandedNode)
        self.usedOperator = dp.usedOperator.copy()
        self.expandedOperator = dp.expandedOperator
        self.Gn = 0
        self.Hn = 0
        
    def saveState(self):
        return self
    
    def returnPuzzle(self):
        return self.currentState
    
    def comparePuzzle(self, left: np.ndarray, right: np.ndarray):
        if (np.array_equal(left, right)): return True
        
    def printCurrState(self):
        print("The puzzle: ")
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