import numpy as np

class savedState():
    def __init__(self, puzzle=np.zeros((3,3))):
        self.currentState = np.copy(puzzle)
        self.usedOperator = []
        self.expandedOperator = ""
        self.Gn = 0
        self.Hn = 0
    
    def returnPuzzle(self):
        return self.currentState
    
    def puzzleInitializer(self, puzzle: np.ndarray):
        self.currentState = np.copy(puzzle)
        
    # return index of zero by (y, x) / ([y][x])
    def findZero(self):
        indexs = np.where(self.currentState == 0)
        #return indexs
        return ((indexs[0])[0], (indexs[1])[0])
    
    def comparePuzzle(self, left: np.ndarray, right: np.ndarray):
        if (np.array_equal(left, right)): return True

    # Print current 3x3 Matrix
    def printCurrState(self):
        print("The puzzle: ")
        print(self.currentState[0])
        print(self.currentState[1])
        print(self.currentState[2])

    # Print Current Operator
    def printCurrOperator(self):
        print("You should not go " + self.expandedOperator + " now")

    # Print g(n) and h(n)
    def printGH(self):
        print("g(n) = ", self.Gn)
        print("h(n) = ", self.Hn)

    # Print all info that can be printed
    def printAll(self):
        self.printCurrState()
        self.printCurrOperator()
        self.printGH()

if __name__ == "__main__":
    temp = savedState(np.array([[1,2,3],[4,5,6],[7,8,0]]))
    temp.printAll()
    a = temp.findZero()
    print(a)



