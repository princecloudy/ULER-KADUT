class Node:
  def __init__(self, data):
    self.data = data
    self.visited = False
    self.neighbors = []  # List to store connected nodes

  def add_neighbor(self, neighbor):
    self.neighbors.append(neighbor)


def dfs(node):
  # Mark the current node as visited
  node.visited = True
  print(node.data, end=" ")  # Process the current node

  # Recursively visit all unvisited neighbors
  for neighbor in node.neighbors:
    if not neighbor.visited:
      dfs(neighbor)


# Create some nodes
node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")

# Add connections between nodes (representing a graph)
node1.add_neighbor(node2)
node1.add_neighbor(node3)
node2.add_neighbor(node4)
node2.add_neighbor(node5)
node3.add_neighbor(node4)
node3.add_neighbor(node6)

# Start DFS from node1
dfs(node1)

print("\n")  # Add a newline for better output formatting




