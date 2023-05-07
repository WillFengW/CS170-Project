import numpy as np
from savedState import savedState
from defaultPuzzle import defaultPuzzle
from puzzleCollector import puzzleCollector

class UniformCostSearch(defaultPuzzle):
    def __init__(self):
        super().__init__()

    def add_child_to_frontier(self, children):
        self.usedStates.extend(children)
        for child in children:
            insert_pos = 0
            #insert child from lowest to highest cost
            while insert_pos < len(self.frontier) and self.frontier[insert_pos].Gn <= child.Gn:
                insert_pos += 1
            self.frontier.insert(insert_pos, child)


    # uniform cost search algorithm (no need to consider costs in this case)
    def run(self):
        # set initial state
        self.initialFrontier()
        while self.frontier:
            self.removeFront()
            self.printPuzzle()
            # check if goal state is reached
            if self.goalTest():
                return True
            # generate children nodes
            children = self.createChildren()
            # add children nodes to frontier
            self.add_child_to_frontier(children)
        return False

