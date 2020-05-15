class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.right.left = Node(6)
tree.right.right = Node(7)
