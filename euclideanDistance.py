import numpy as np
import math
from defaultPuzzle import defaultPuzzle

class euclideanDistance():
    def __init__(self, puzzle: np.ndarray):
        self.d = defaultPuzzle(puzzle)


    # get index in 3x3 array by number
    # [1, 2, 3]
    # [4, 5, 6]
    # [7, 8, 9]
    def getCorrectPosition(self, n: int):
        if (n == 1):
            return [0, 0]

        if (n == 2):
            return [0, 1]

        if (n == 3):
            return [0, 2]
            
        if (n == 4):
            return [1, 0]

        if (n == 5):
            return [1, 1]

        if (n == 6):
            return [1, 2]

        if (n == 7):
            return [2, 0]

        if (n == 8):
            return [2, 1]

        if (n == 9):
            return [2, 2]
        
        return [0, 0]
            
    # getHn base on the distance from wrong puzzle to the correct puzzle
    def getHn(self, puzzle: np.ndarray):
        sum = 0.0
        correctNumber = 1
        for y in range(3):
            for x in range(3):
                currentNumber = puzzle[y][x]
                if(currentNumber != correctNumber):
                    a = [x, y]
                    b = self.getCorrectPosition(currentNumber)
                    sum += math.dist(a, b)
                correctNumber += 1
        return sum

    # get the state that have lowest cost in frontier, then remove it from frontier
    # and let it become expandedNode
    def getMinState(self, states):
        self.d.expandedNode = states[0]
        minIndex = 0
        i = 0
        if (states):
            for state in states:
                state.Hn = self.getHn(state.currentState)
                if(state.Hn + state.Gn <= self.d.expandedNode.Hn + self.d.expandedNode.Gn):
                    self.d.expandedNode = state
                    minIndex = i
                i += 1
        #print("minIndex: ", minIndex + 1)       
        self.d.removeState(minIndex)

        

    # run the algorithm
    def run(self):
        self.d.initialFrontier()
        self.d.printFrontier()
        i = 1
        while (not self.d.goalTest()):
            if not self.d.frontier:
                print("no solution")
                return False
            print(" ")
            self.getMinState(self.d.frontier)
            self.d.pushFrontier(self.d.createChildren())
            self.d.printPuzzle()
            #self.d.printFrontier()
            i += 1
        print("The final solution is: ", self.d.expandedNode.usedOperator)
        print("Total node: ", self.d.nodeCount)
        print("The Max Queue Size: ", self.d.maxSize)
        return True

if __name__ == "__main__":
    e = euclideanDistance()
    result = e.run()
    if(result):
        print("The final solution is:")
        e.d.printPuzzle()
    else:
        print("no solution")

    