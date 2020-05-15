class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
def insert(root, data):
    if root is None:
        root = Node(data)
    else:
        if root.data > data:
            if root.left is None:
                root.left = Node(data)
            else:
                insert(root.left, data)
        else:
            if root.right is None:
                root.right = Node(data)
            else:
                insert(root.right, data)
    return
# Example
nums = [1,2,3,4,5,6,7]
root = len(nums) // 2
# Root node
tree = Node(nums[root])
# Left tree
for num in nums[:root]:
    insert(tree, num)
# Right tree
for num in nums[root+1:]:
    insert(tree, num)
 
# Print tree (pre_order traversal)
def pre_order(tree):
    if not tree:
        return
    else:
        print(tree.data)
        pre_order(tree.left)
        pre_order(tree.right)
    return
pre_order(tree)
