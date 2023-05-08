from Node import Node
from savedState import savedState
import numpy as np

class Tree:
    def __init__(self):
        self.start = Node()
        self.root = self.start

    def addNode(self, puzzle: np.ndarray):
        curr_node = self.root
        for row in puzzle:
            for element in row:
                if element == 1:
                    if curr_node.one is None:
                        curr_node.one = Node()
                    curr_node = curr_node.one
                elif element == 2:
                    if curr_node.two is None:
                        curr_node.two = Node()
                    curr_node = curr_node.two
                elif element == 3:
                    if curr_node.three is None:
                        curr_node.three = Node()
                    curr_node = curr_node.three
                elif element == 4:
                    if curr_node.four is None:
                        curr_node.four = Node()
                    curr_node = curr_node.four
                elif element == 5:
                    if curr_node.five is None:
                        curr_node.five = Node()
                    curr_node = curr_node.five
                elif element == 6:
                    if curr_node.six is None:
                        curr_node.six = Node()
                    curr_node = curr_node.six
                elif element == 7:
                    if curr_node.seven is None:
                        curr_node.seven = Node()
                    curr_node = curr_node.seven
                elif element == 8:
                    if curr_node.eight is None:
                        curr_node.eight = Node()
                    curr_node = curr_node.eight
                elif element == 0:
                    if curr_node.zero is None:
                        curr_node.zero = Node()
                    curr_node = curr_node.zero

    def findNode(self, puzzle: np.ndarray):
        curr_node = self.root
        for row in puzzle:
            for element in row:
                if element == 1:
                    if curr_node.one is None:
                        return False
                    curr_node = curr_node.one
                elif element == 2:
                    if curr_node.two is None:
                        return False
                    curr_node = curr_node.two
                elif element == 3:
                    if curr_node.three is None:
                        return False
                    curr_node = curr_node.three
                elif element == 4:
                    if curr_node.four is None:
                        return False
                    curr_node = curr_node.four
                elif element == 5:
                    if curr_node.five is None:
                        return False
                    curr_node = curr_node.five
                elif element == 6:
                    if curr_node.six is None:
                        return False
                    curr_node = curr_node.six
                elif element == 7:
                    if curr_node.seven is None:
                        return False
                    curr_node = curr_node.seven
                elif element == 8:
                    if curr_node.eight is None:
                        return False
                    curr_node = curr_node.eight
                elif element == 0:
                    if curr_node.zero is None:
                        return False
                    curr_node = curr_node.zero
        return True

if __name__ == "__main__":
    a = np.array([[1, 2, 3], [4, 8, 0], [7, 6, 5]])
    b = np.array([[4, 2, 3], [1, 8, 0], [7, 6, 5]])
    c = np.array([[4, 2, 3], [1, 8, 0], [6, 7, 5]])
    t = Tree()
    t.addNode(a)
    t.addNode(b)
    print(t.findNode(a))
    print(t.findNode(c))







