import numpy as np
import math
from defaultPuzzle import defaultPuzzle

class euclideanDistance(defaultPuzzle):
    def __init__(self):
        d = defaultPuzzle()

    def distance(x1, y1, x2, y2):
        a = [x1, y1]
        b = [x2, y2]
        return math.dist(a, b)

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
            

    def getHn(self, puzzle: np.ndarray):
        sum = 0
        correctNumber = 1
        for y in range(3):
            for x in range(3):
                currentNumber = puzzle[y][x]
                if(currentNumber != correctNumber):
                    a = [x, y]
                    b = self.getCorrectPosition(currentNumber)
                    sum += math.dist(a, b)
        return sum

    def getMinState(self, states: defaultPuzzle.frontier):
        self.d.expandedNode = states[0]
        minIndex = 0
        i = 0
        for state in states:
            state.Hn = self.getHn(state.currentState)
            if(state.Hn + state.Gn <= self.d.expandedNode.Hn + self.d.expandedNode.Gn):
                self.d.expandedNode = state
                minIndex = i
            i += 1
        self.d.removeState(minIndex)

    def run(self):
        self.d.initialFrontier()
        while (not self.d.goalTest()):
            if not self.d.frontier:
                return False
            self.getMinState(self.d.frontier)
            self.d.pushFrontier(self.d.createChildren())
            self.d.printPuzzle()
            self.d.printFrontier()
        return True

if __name__ == "__main__":
    e = euclideanDistance()
    result = e.run()
    if(result):
        print(*e.d.usedOperator, sep = ", ")
    else:
        print("no solution")

    