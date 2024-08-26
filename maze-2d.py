class Maze:
  def __init__(self, maze_map):
    self.maze_map = maze_map
    self.rows = len(maze_map[0])
    self.cols = len(maze_map[0])

  def is_valid_cell(self, row, col):
    return 0 <= row < self.rows and 0 <= col < self.cols and self.maze_map[row][col] != "X"

  def dfs_solve(self, row, col, path):
    stack = [(row, col)]
    visited = set() 

    while stack:
      row, col = stack.pop() 
      if self.maze_map[row][col] == "E":
        path.append((row, col))
        return True
      elif (row, col) not in visited:
        if self.maze_map[row][col] != "S":
          visited.add((row, col)) 
          self.maze_map[row][col] = "V"  

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
          new_row, new_col = row + dx, col + dy
          if self.is_valid_cell(new_row, new_col):
            stack.append((new_row, new_col))
            path.append((row, col))

    return False 

  def print_maze(self):
    for row in self.maze_map:
      for cell in row:
        if cell == "X":
          print("#", end=" ")  
        elif cell == "V":
          print("*", end=" ") 
        elif cell == "S":
          print("S", end=" ")  
        elif cell == "E":
          print("E", end=" ")  
        else:
          print(".", end=" ")  
      print()

    if "S" not in [cell for row in self.maze_map for cell in row]:
      print("Error: Start position 'S' not found")


  def solve(self):
    start_row, start_col = None, None
    for row in range(self.rows):
      for col in range(self.cols):
        if self.maze_map[row][col] == "S":
          start_row, start_col = row, col
          break

    if start_row is None or start_col is None:
      print("Error: Start position 'S' not found")
      return

    path = [] 
    if self.dfs_solve(start_row, start_col, path):
      print("Maze solved! Path:", path)
      self.print_maze()  
    else:
      print("Maze cannot be solved!")

maze_map = [
  ["S", ".", "X", ".", "."],
  [".", "X", "X", ".", "X"],
  [".", ".", ".", ".", "."],
  [".", ".", "X", "X", "."],
  ["X", "X", ".", ".", "E"],
]

maze = Maze(maze_map)
maze.solve()