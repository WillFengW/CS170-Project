import numpy as np
from savedState import savedState

class defaultPuzzle(savedState):
    def __init__(self):
        self.initialState = savedState(np.array([[1,2,3],[4,8,0],[7,6,5]]))
        self.goalState = savedState(np.array([[1,2,3],[4,5,6],[7,8,0]]))
        
        self.expandedNode = savedState()
        self.frontier = []
        self.usedStates = []
        self.usedOperator = []
        self.expandedOperator = ""
        
    # print the puzzle in expanded node
    def printPuzzle(self):
        print("The Puzzle in expanded node:")
        print(self.expandedNode.currentState[0])
        print(self.expandedNode.currentState[1])
        print(self.expandedNode.currentState[2])
        print("Previous Steps: ", self.expandedNode.usedOperator)
        print("Last Step: ", self.expandedNode.expandedOperator)
        print("G(n): ", self.expandedNode.Gn)
        print("H(n): ", self.expandedNode.Hn)
        
    # print all nodes in the frontier
    def printFrontier(self):
        for number, puzzle in enumerate(self.frontier):
            print("The puzzle ", number+1)
            print(puzzle.currentState[0])
            print(puzzle.currentState[1])
            print(puzzle.currentState[2])
        
    # get the initial frontier, run before everything
    def initialFrontier(self):
        self.frontier.append(self.initialState)
        self.usedStates.append(self.initialState)
        
    # Test if the node equal to the goal state
    def goalTest(self) -> bool:
        if (np.array_equal(self.expandedNode.currentState, self.goalState.currentState)): return True
        
    # get the first array from frontier
    def removeFront(self):
        if (self.frontier): 
            self.expandedNode = self.frontier.pop(0)
            if (self.usedOperator):
                self.expandedOperator = self.usedOperator.pop(0)
        else: print("The Frontier is Empty!\n")

    # remove select state from frontier
    def removeState(self, i: int):
        if (self.frontier): 
            del self.frontier[i]
        else: print("The Frontier is Empty!\n")
        
    # push any children nodes to frontier
    def pushFrontier(self, children: list):
        self.frontier.extend(children)
        self.usedStates.extend(children)
        
    # find the index of number 0, you should not use this directly
    def findIndex(self):
        return np.where(self.expandedNode.currentState == 0)
        
    # move 0 up, you should not use this directly
    def moveUp(self, y: int, x: int):
        node = savedState(np.copy(self.expandedNode.currentState))
        node.Gn = self.expandedNode.Gn + 1
        node.usedOperator = self.expandedNode.usedOperator.copy()
        tmp = node.currentState
        tmp[y][x], tmp[y-1][x] = tmp[y-1][x], tmp[y][x]
        return node
    
    # move 0 down, you should not use this directly
    def moveDown(self, y: int, x: int):
        node = savedState(np.copy(self.expandedNode.currentState))
        node.Gn = self.expandedNode.Gn + 1
        node.usedOperator = self.expandedNode.usedOperator.copy()
        tmp = node.currentState
        tmp[y][x], tmp[y+1][x] = tmp[y+1][x], tmp[y][x]
        return node
    
    # move 0 right, you should not use this directly
    def moveRight(self, y: int, x: int):
        node = savedState(np.copy(self.expandedNode.currentState))
        node.Gn = self.expandedNode.Gn + 1
        node.usedOperator = self.expandedNode.usedOperator.copy()
        tmp = node.currentState
        tmp[y][x], tmp[y][x+1] = tmp[y][x+1], tmp[y][x]
        return node
    
    # move 0 left, you should not use this directly
    def moveLeft(self, y: int, x: int):
        node = savedState(np.copy(self.expandedNode.currentState))
        node.Gn = self.expandedNode.Gn + 1
        node.usedOperator = self.expandedNode.usedOperator.copy()
        tmp = node.currentState
        tmp[y][x], tmp[y][x-1] = tmp[y][x-1], tmp[y][x]
        return node

    # check duplicate or not
    def checkDuplicate(self, puzzle: np.ndarray):
        for state in self.usedStates:
            if (np.array_equal(state.currentState, puzzle)):
                return False    # duplicate
        return True     # not duplicate

    # find any possible children of expanded node
    def createChildren(self):
        indexs = self.findIndex()
        (y, x) = indexs[0][0], indexs[1][0]
        up = True
        down = True
        right = True
        left = True
        children = []
        
        # at top line
        if (y == 0):
            up = False
        
        # at bottom line
        if (y == 2):
            down = False

        # at left line
        if (x == 0):
            left = False

        # at right line
        if (x == 2):
            right = False

        if (self.expandedNode.expandedOperator == "up"):
            down = False

        if (self.expandedNode.expandedOperator == "down"):
            up = False

        if (self.expandedNode.expandedOperator == "right"):
            left = False

        if (self.expandedNode.expandedOperator == "left"):
            right = False

        # check dulicate or not
        if (up):
            newState = self.moveUp(y, x)
            if (self.checkDuplicate(newState)):
                newState.usedOperator.append("up")
                newState.expandedOperator = "up"
                children.append(newState)
        
        if (down):
            newState = self.moveDown(y, x)
            if (self.checkDuplicate(newState)):
                newState.usedOperator.append("down")
                newState.expandedOperator = "down"
                children.append(newState)
                

        if (right):
            newState = self.moveRight(y, x)
            if (self.checkDuplicate(newState)):
                newState.usedOperator.append("right")
                newState.expandedOperator = "right"
                children.append(newState)

        if (left):
            newState = self.moveLeft(y, x)
            if (self.checkDuplicate(newState)):
                newState.usedOperator.append("left")
                newState.expandedOperator = "left"
                children.append(newState)

        return children
    
    # return expandedNode
    def returnExpndNode(self):
        return self.expandedNode
    
if __name__ == "__main__":
    d = defaultPuzzle()
    print(d.expandedNode.currentState)
    d.initialFrontier()
    d.printFrontier()
    d.removeFront()
    d.printPuzzle()
    d.pushFrontier(d.createChildren())
    d.printFrontier()
    d.removeFront()
    d.printPuzzle()
    d.pushFrontier(d.createChildren())
    d.printFrontier()
    