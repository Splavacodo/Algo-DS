from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        val_to_idx = {val: idx for idx, val in enumerate(inorder)}
        preorder = deque(preorder)

        def tree_builder(start, end): 
            if start > end:
                return None
            
            root = TreeNode(preorder.popleft())
            mid = val_to_idx[root.val]

            root.left = tree_builder(start, mid - 1)
            root.right = tree_builder(mid + 1, end)

            return root
        
        return tree_builder(0, len(preorder) - 1)