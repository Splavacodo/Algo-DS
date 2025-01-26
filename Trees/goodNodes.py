class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = []
        stack.append((root, root.val))

        good_nodes = 0

        while stack:
            curr_node, max_so_far = stack.pop()

            if curr_node.val >= max_so_far:
                good_nodes += 1
                max_so_far = curr_node.val
            
            if curr_node.left:
                stack.append((curr_node.left, max_so_far))
            if curr_node.right:
                stack.append((curr_node.right, max_so_far))
        
        return good_nodes