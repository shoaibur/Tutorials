class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def max_depth_binary_tree(tree):
    if not tree:
        return 0
    left_depth = max_depth_binary_tree(tree.left)
    right_depth = max_depth_binary_tree(tree.right)
    return max(left_depth, right_depth) + 1
    
