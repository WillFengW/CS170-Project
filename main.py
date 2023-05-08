from puzzleCollector import puzzleCollector
from savedState import savedState
from defaultPuzzle import defaultPuzzle
from uniformCost import UniformCostSearch
from euclideanDistance import euclideanDistance
from misplacedTile import misplacedTile
import numpy as np
import time

def defaultPuzzleList():
    puzzleList = []
    trival = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    veryEasy = np.array([[1, 2, 3], [4, 5, 6], [7, 0, 8]])
    easy = np.array([[1, 2, 0], [4, 5, 3], [7, 8, 6]])
    doable = np.array([[0, 1, 2], [4, 5, 3], [7, 8, 6]])
    oh_Boy = np.array([[8, 7, 1], [6, 0, 2], [5, 4, 3]])
    impossible = np.array([[1, 2, 3], [4, 5, 6], [8, 7, 0]])
    example = np.array([[1, 2, 3], [4, 8, 0], [7, 6, 5]])
    puzzleList.extend(
        [trival, veryEasy, easy, doable, oh_Boy, impossible, example])  # Use extend instead of append for multiple elements
    return puzzleList

def printDefaultPuzzles(puzzleList):
    for i, puzzle in enumerate(puzzleList):
        print("Puzzle", i + 1)
        print(puzzle)
    user_input = input("Enter the puzzle number you want to solve: ")
    return int(user_input)

def main():
    puzzle_choice = 0
    choice = ""
    while choice != "3":
        print("Welcome to Team_22's 8-puzzle solver.\n"
              "--------Menu-------\n"
              "1, Choose a Default puzzle\n"
              "2, Enter your own puzzle\n"
              "3, Quit\n"
              "-------------------\n")
        choice = input("Enter your choice: ")
        dp = puzzleCollector()
        if choice == "1":
            puzzles = defaultPuzzleList()
            puzzle_choice = printDefaultPuzzles(puzzles)
            subMenu(puzzles[puzzle_choice-1])
            break
        elif choice == "2":
            subMenu(dp.setPuzzle())
            break
        elif choice == "3":
            print("See you!")
        else:
            print("wrong option!")


def subMenu(puzzle: np.ndarray):
    choice = ""
    while choice != "4":
        print("\n-------------------------------------------\n"
              "Enter your choice of algorithm: \n"
              "1, Uniform Cost Search\n"
              "2, A* with the Misplaced Tile heuristic\n"
              "3, A* with the Euclidean distance heuristic\n"
              "4, Quit\n"
              "-------------------------------------------\n")
        choice = input("Enter your choice of algorithm: ")

        if choice == "1":
            print("Using Uniform Cost Search......")
            ucs = UniformCostSearch(puzzle)
            start_time = time.time()
            ucs.run()
            print("--- %s seconds used ---" % (time.time() - start_time))
            break
        elif choice == "2":
            print("Using A* with the Misplaced Tile heuristic......")
            m = misplacedTile(puzzle)
            start_time = time.time()
            m.run()
            print("--- %s seconds used ---" % (time.time() - start_time))
            break
        elif choice == "3":
            print("Using A* with the Euclidean distance heuristic......")
            e = euclideanDistance(puzzle)
            start_time = time.time()
            e.run()
            print("--- %s seconds used ---" % (time.time() - start_time))
            break
        elif choice == "4":
            print("See you......")
        else:
            print("wrong option!")


if __name__ == "__main__":
    main()