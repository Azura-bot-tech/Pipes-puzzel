from data import TESTCASE
from solver import SearchPuzzle
import time
import tracemalloc
import matplotlib.pyplot as plt

class PipesPuzzle:
    def __init__(self, level):
        self.init_state = None
        self.level = level
        self.create_puzzle()
        self.path = []
        self.dataForPlot = []
    
    def create_puzzle(self):
        """
        Generate level and init_state from GOAL_STATES
        """
        if self.level > 7:
            quit()
        testcase = TESTCASE[f"level{self.level}"]
        self.init_state = testcase

    def solve(self, solve_choice):
        solver = SearchPuzzle()
        start_time = time.time()
        tracemalloc.start()
        if solve_choice == 1:
            self.path = solver.solve_dfs(self.init_state)
        elif solve_choice == 2:
            temp = solver.solve_Astar(self.init_state)
            self.dataForPlot = temp[0]
            self.path = temp[1]
        else:
            print("You must choose 1 for DFS or 2 for A*.")
            exit(1)
        execution_time = round(time.time() - start_time, 4)
        memory = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        print("Execution time: ", str(execution_time))
        print("Memory used: ", round(memory/(2**20), 2), " MB")
        return execution_time, memory
        

    def simulatePlot(self):
        plt.bar(*zip(*self.dataForPlot.items()))
        plt.xlabel('Number of step')
        plt.ylabel('Number of searching in step')
        plt.title('Statistics')
        plt.show()       