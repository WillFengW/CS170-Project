import numpy as np
from defaultPuzzle import defaultPuzzle
from savedState import savedState


class puzzleCollector(defaultPuzzle):
    def __init__(self):
        super().__init__(np.zeros((3,3)))

    def setPuzzle(self):
    # get the user input
        row_numbers = []
        print("Enter your puzzle, use a zero to represent the blank (numbers cannot be repeated)")
        for i in range(3):
            row = input(f"Enter the {i + 1} row, use space or tabs between numbers: ")
            for num_str in row.split():
                num = int(num_str)
                row_numbers.append(num)
        return np.array(row_numbers).reshape(3, 3)  #ref: https://stackoverflow.com/questions/28205805/how-do-i-create-3x3-matrices


        
        