class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root: TreeNode) -> int: 
    def dfs(node: TreeNode) -> int: 
        nonlocal diameter
        # Base case will return 0 
        if not node: 
            return 0
        
        # Traverse the tree to the max depth
        leftDepth = dfs(node.left)
        rightDepth = dfs(node.right)
        
        diameter = max(diameter, leftDepth + rightDepth)

        return max(leftDepth, rightDepth) + 1
    
    diameter = 0
    dfs(root)
    return diameter