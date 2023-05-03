import numpy as np
import re

class defaultPuzzle():
    def __init__(self):
        self.initialState = np.array([[1,2,0],[4,5,3],[7,8,6]])
        self.goalState = np.array([[1,2,3],[4,5,6],[7,8,0]])
        self.expandedNode = np.zeros((3,3))
        self.frontier = []
        self.usedOperator = []
        self.expandedOperator = ""
        
    # print the puzzle in expanded node
    def printPuzzle(self):
        print("The Puzzle in expanded node:")
        print(self.expandedNode[0])
        print(self.expandedNode[1])
        print(self.expandedNode[2])
        
    # print all nodes in the frontier
    def printFrontier(self):
        for number, puzzle in enumerate(self.frontier):
            print("The puzzle ", number+1)
            print(puzzle[0])
            print(puzzle[1])
            print(puzzle[2])
        
    # get the initial frontier, run before everything
    def initialFrontier(self):
        self.frontier.append(self.initialState)
        
    # Test if the node equal to the goal state
    def goalTest(self) -> bool:
        if (np.array_equal(self.expandedNode, self.goalState)): return True
        
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
        return np.where(self.expandedNode == 0)
        
    # move 0 up, you should not use this directly
    def moveUp(self, y: int, x: int):
        tmp = np.copy(self.expandedNode)
        tmp[y][x], tmp[y-1][x] = tmp[y-1][x], tmp[y][x]
        return tmp
    
    # move 0 down, you should not use this directly
    def moveDown(self, y: int, x: int):
        tmp = np.copy(self.expandedNode)
        tmp[y][x], tmp[y+1][x] = tmp[y+1][x], tmp[y][x]
        return tmp
    
    # move 0 right, you should not use this directly
    def moveRight(self, y: int, x: int):
        tmp = np.copy(self.expandedNode)
        tmp[y][x], tmp[y][x+1] = tmp[y][x+1], tmp[y][x]
        return tmp
    
    # move 0 left, you should not use this directly
    def moveLeft(self, y: int, x: int):
        tmp = np.copy(self.expandedNode)
        tmp[y][x], tmp[y][x-1] = tmp[y][x-1], tmp[y][x]
        return tmp

    # find any possible children of expanded node
    def createChildren(self):
        indexs = self.findIndex()
        (y, x) = indexs[0][0], indexs[1][0]
        children = []
        
        
        if (y == 0 and self.expandedOperator != "down"):
            children.append(self.moveDown(y, x))
            self.usedOperator.append("up")
        if (y == 1):
            if (self.expandedOperator != "down"):
                children.append(self.moveDown(y, x))
                self.usedOperator.append("up")
            if (self.expandedOperator != "up"):
                children.append(self.moveUp(y, x))
                self.usedOperator.append("down")
        if (y == 2 and self.expandedOperator != "up"):
            children.append(self.moveUp(y, x))
            self.usedOperator.append("down")
            
        if (x == 0 and self.expandedOperator != "right"):
            children.append(self.moveRight(y, x))
            self.usedOperator.append("left")
        if (x == 1):
            if (self.expandedOperator != "right"):
                children.append(self.moveRight(y, x))
                self.usedOperator.append("left")
            if (self.expandedOperator != "left"):
                children.append(self.moveLeft(y, x))
                self.usedOperator.append("right")
        if (x == 2 and self.expandedOperator != "left"):
            children.append(self.moveLeft(y, x))
            self.usedOperator.append("right")
        
        return children
    
if __name__ == "__main__":
    d = defaultPuzzle()
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
    