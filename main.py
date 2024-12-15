# Source code tham khảo từ https://github.com/khoavukhoa3004/CO3061-AI-Puzzle-Pipes

from puzzle import PipesPuzzle
from ui import PuzzleInterface, SelectionInterface

if __name__ == "__main__":
  selection_interface = SelectionInterface()
  config = selection_interface.run()
  puzzle_pipes = PipesPuzzle(config[1])
  time, memory = puzzle_pipes.solve(config[0])
  puzzle_interface = PuzzleInterface(puzzle_pipes, time, memory)
  puzzle_interface.run()
  if len(puzzle_pipes.dataForPlot) != 0:
    t = input("Show statistics about heuristic searching ? (Y: Yes, other: No)")
    if t == 'Y' or t =='y':
      puzzle_pipes.simulatePlot()

