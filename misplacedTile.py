import numpy as np
import math
from savedState import savedState
from defaultPuzzle import defaultPuzzle

class misplacedTile():
    def __init__(self):
        self.df = defaultPuzzle()

    # get the number of misplaced tiles
    def getMatrixDiff(self, matrix: np.ndarray):
        temp_matrix = self.df.goalState.returnPuzzle()
        counter = 0
        for i in range(3):
            for j in range(3):
                if matrix[i][j] == 0:
                    continue
                if matrix[i][j] != temp_matrix[i][j]:
                    counter = counter + 1
        return counter

    # Quick calculating function for f(n)
    def get_fn(self, state: savedState):
        return (state.Hn + state.Gn)

    # get the state with lowest f(n)
    def getMinState(self):
        position = 0
        count = 0
        temp = self.df.frontier[0]
        for state in self.df.frontier:
            state.Hn = self.getMatrixDiff(state.currentState)
            if self.get_fn(state) < self.get_fn(temp):
                temp = state
                # It is used for removing the chosen state in frontier
                position = count
            count += 1
        self.df.expandedNode = temp
        self.df.removeState(position)

    def run(self):
        self.df.initialFrontier()
        self.df.printFrontier()
        i = 1
        while (not self.df.goalTest()):
            if not self.df.frontier:
                return False
            print(i, " round")
            self.getMinState()
            self.df.pushFrontier(self.df.createChildren())
            self.df.printPuzzle()
            # self.d.printFrontier()
            i += 1
        return True


if __name__ == "__main__":
    m = misplacedTile()
    result = m.run()
    if (result):
        print("The final solution is:")
        m.df.printPuzzle()
    else:
        print("no solution")
    """
    t = misplacedTile()
    a = np.array([[1,2,3],[4,8,0],[7,6,5]])
    b = t.getMatrixDiff(a)
    print(b)
    """