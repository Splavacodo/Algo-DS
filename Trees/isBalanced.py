'''
Given a binary tree, determine if it is height-balanced.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# def isBalanced(root: TreeNode) -> bool: 
#     def dfs(node: TreeNode) -> int: 
#         nonlocal balanced
#         if not node: 
#             return 0
        
#         leftHeight = dfs(node.left)
#         rightHeight = dfs(node.right)

#         if abs(leftHeight - rightHeight) > 1: 
#             balanced = False 
        
#         return 1 + max(leftHeight, rightHeight)
 
#     balanced = True
#     dfs(root)
#     return balanced

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        Reattempt at isBalanced

        Date: 12/02/24
        """
        def get_height(node):
            if node is None:
                return 0
            return max(get_height(node.left), get_height(node.right)) + 1
        
        if root is None:
            return True
        
        left_height = get_height(root.left)
        right_height = get_height(root.right)

        if abs(right_height - left_height) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)