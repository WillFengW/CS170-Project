import numpy as np
from savedState import savedState

class defaultPuzzle(savedState):
    def __init__(self):
        self.initialState = savedState(np.array([[1,2,0],[4,5,3],[7,8,6]]))
        self.goalState = savedState(np.array([[1,2,3],[4,5,6],[7,8,0]]))
        
        self.expandedNode = savedState()
        self.frontier = []
        self.usedOperator = []
        self.expandedOperator = ""
        
    # print the puzzle in expanded node
    def printPuzzle(self):
        print("The Puzzle in expanded node:")
        print(self.expandedNode.currentState[0])
        print(self.expandedNode.currentState[1])
        print(self.expandedNode.currentState[2])
        
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
        
    # push any children nodes to frontier
    def pushFrontier(self, children: list):
        self.frontier.extend(children)
        
    # find the index of number 0, you should not use this directly
    def findIndex(self):
        return np.where(self.expandedNode.currentState == 0)
        
    # move 0 up, you should not use this directly
    def moveUp(self, y: int, x: int):
        node = savedState(np.copy(self.expandedNode.currentState))
        tmp = node.currentState
        tmp[y][x], tmp[y-1][x] = tmp[y-1][x], tmp[y][x]
        return node
    
    # move 0 down, you should not use this directly
    def moveDown(self, y: int, x: int):
        node = savedState(np.copy(self.expandedNode.currentState))
        tmp = node.currentState
        tmp[y][x], tmp[y+1][x] = tmp[y+1][x], tmp[y][x]
        return node
    
    # move 0 right, you should not use this directly
    def moveRight(self, y: int, x: int):
        node = savedState(np.copy(self.expandedNode.currentState))
        tmp = node.currentState
        tmp[y][x], tmp[y][x+1] = tmp[y][x+1], tmp[y][x]
        return node
    
    # move 0 left, you should not use this directly
    def moveLeft(self, y: int, x: int):
        node = savedState(np.copy(self.expandedNode.currentState))
        tmp = node.currentState
        tmp[y][x], tmp[y][x-1] = tmp[y][x-1], tmp[y][x]
        return node

    # find any possible children of expanded node
    def createChildren(self):
        indexs = self.findIndex()
        (y, x) = indexs[0][0], indexs[1][0]
        children = []
        
        
        if (y == 0 and self.expandedOperator != "up"):
            children.append(self.moveDown(y, x))
            self.usedOperator.append("down")
        if (y == 1):
            if (self.expandedOperator != "up"):
                children.append(self.moveDown(y, x))
                self.usedOperator.append("down")
                
            if (self.expandedOperator != "down"):
                children.append(self.moveUp(y, x))
                self.usedOperator.append("up")
        if (y == 2 and self.expandedOperator != "down"):
            children.append(self.moveUp(y, x))
            self.usedOperator.append("up")
            
        if (x == 0 and self.expandedOperator != "left"):
            children.append(self.moveRight(y, x))
            self.usedOperator.append("right")
        if (x == 1):
            if (self.expandedOperator != "left"):
                children.append(self.moveRight(y, x))
                self.usedOperator.append("right")
                
            if (self.expandedOperator != "right"):
                children.append(self.moveLeft(y, x))
                self.usedOperator.append("left")
        if (x == 2 and self.expandedOperator != "right"):
            children.append(self.moveLeft(y, x))
            self.usedOperator.append("left")
        
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
    