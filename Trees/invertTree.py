class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Iterative
def invertTree(root: TreeNode) -> TreeNode: 
    if not root: 
        return None

    # Stop at each node that has a child and switch their left and right child
    nodeStack = []
    nodeStack.append(root)
    
    while nodeStack: 
        currNode = nodeStack.pop()
        if currNode.left and currNode.right: 
            currNode.left, currNode.right = currNode.right, currNode.left
            nodeStack.append(currNode.left)
            nodeStack.append(currNode.right)
        elif currNode.left and not currNode.right: 
            currNode.right = currNode.left
            currNode.left = None
            nodeStack.append(currNode.right)
        elif not currNode.left and currNode.right: 
            currNode.left = currNode.right
            currNode.right = None
            nodeStack.append(currNode.left)
        
    return root

# Recursive (DFS)
def invertTree(root: TreeNode) -> TreeNode: 
    if not root: 
        return None
    
    root.left, root.right = root.right, root.left

    invertTree(root.left)
    invertTree(root.right)

    return root