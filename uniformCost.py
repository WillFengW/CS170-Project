import numpy as np
from savedState import savedState
from defaultPuzzle import defaultPuzzle
from puzzleCollector import puzzleCollector

class UniformCostSearch():
    def __init__(self, puzzle: np.ndarray):
        self.df = defaultPuzzle(puzzle)

    def add_child_to_frontier(self, children):
        self.df.usedStates.extend(children)
        for child in children:
            insert_pos = 0
            #insert child from lowest to highest cost
            while insert_pos < len(self.df.frontier) and self.df.frontier[insert_pos].Gn <= child.Gn:
                insert_pos += 1
            self.df.frontier.insert(insert_pos, child)
        sizeQ = len(self.df.frontier)
        if sizeQ > self.df.maxSize: self.df.maxSize = sizeQ


    # uniform cost search algorithm (no need to consider costs in this case)
    def run(self):
        # set initial state
        self.df.initialFrontier()
        while self.df.frontier:
            self.df.removeFront()
            self.df.printPuzzle()
            # check if goal state is reached
            if self.df.goalTest():
                print("The final solution is: ", self.df.expandedNode.usedOperator)
                print("Total node: ", self.df.nodeCount)
                print("The Max Queue Size: ", self.df.maxSize)
                return True
            # generate children nodes
            children = self.df.createChildren()
            # add children nodes to frontier
            self.add_child_to_frontier(children)
            self.df.nodeCount += len(children)
        print("no solution")
        return False

