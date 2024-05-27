class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: TreeNode) -> TreeNode: 
    # Base case will check if the currNode is None
    if not root: 
        return 0
    
    # Find the max height of the left and right subtrees
    leftMax = maxDepth(root.left) + 1
    rightMax = maxDepth(root.right) + 1

    return max(leftMax, rightMax)
    