from puzzleCollector import puzzleCollector


def main():
    choice = ""
    dp = puzzleCollector()
    while choice != "3":
        print("Welcome to XXX (change this to your student ID) 8 puzzle solver.\n"
            "--------Menu-------\n"
            "1, Default puzzle\n"
            "2, Enter new puzzle\n"
            "3, Quit\n"
            "-------------------\n")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            subMenu()
            break
        elif choice == "2":
            subMenu()
            break
        elif choice == "3":
            print("See you!")
        else:
            print("wrong option!")
        
def subMenu():
    choice = ""
    while choice != "4":
        print("\n-------------------------------------------\n"
            "1, Uniform Cost Search\n"
            "2, A* with the Misplaced Tile heuristic\n"
            "3, A* with the Euclidean distance heuristic\n"
            "4, Quit\n"
            "-------------------------------------------\n")
        choice = input("Enter your choice of algorithm: ")
        
        if choice == "1":
            print("Using Uniform Cost Search......")
            break
        elif choice == "2":
            print("Using A* with the Misplaced Tile heuristic......")
            break
        elif choice == "3":
            print("Using A* with the Euclidean distance heuristic......")
            break
        elif choice == "4":
            print("See you......")
        else:
            print("wrong option!")
    
    
if __name__ == "__main__":
    main()