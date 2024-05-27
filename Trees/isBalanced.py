'''
Given a binary tree, determine if it is height-balanced.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root: TreeNode) -> bool: 
    def dfs(node: TreeNode) -> int: 
        nonlocal balanced
        if not node: 
            return 0
        
        leftHeight = dfs(node.left)
        rightHeight = dfs(node.right)

        if abs(leftHeight - rightHeight) > 1: 
            balanced = False 
        
        return 1 + max(leftHeight, rightHeight)
 
    balanced = True
    dfs(root)
    return balanced