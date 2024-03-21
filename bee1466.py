"""Beecrowd | 1466"""


# Tree implementation
class Node:
    """Tree node implementation"""
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data) -> None:
        """Insert method"""
        if self.data is not None:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


# BFS serach function
def bfs_with_nodes(root_node: Node):
    """BFS search from the root node"""
    visited = []
    fifo_to_visit = []
    fifo_to_visit.append(root_node)

    while (len(fifo_to_visit) > 0):
        curr = fifo_to_visit.pop(0)
        visited.append(curr.data)
        if curr.left is not None:
            fifo_to_visit.append(curr.left)
        if curr.right is not None:
            fifo_to_visit.append(curr.right)
    return visited


# global steps
cases_num = int(input())
visits = []

for i in range(cases_num):
    tree_elem_num = int(input())
    values = [int(x) for x in input().split(' ')]
    # FIFO of nodes pointers
    fifo = []
    root = Node()
    # Populates the tree
    for value in values:
        root.insert(value)

    visits.append(bfs_with_nodes(root))

# Prints final answer
for i, visit in enumerate(visits):
    print(f"Case {i + 1}:")
    print(str(visit)
          .replace("[", "")
          .replace("]", "")
          .replace(",", ""))
    print()
