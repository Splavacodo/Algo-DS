class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        level_order = []
        self.visit(root, 0, level_order)

        return level_order

    def visit(self, node, level, node_list):
        if not node:
            return
        
        if len(node_list) <= level:
            node_list.append([])
        
        node_list[level].append(node.val)
        self.visit(node.left, level + 1, node_list)
        self.visit(node.right, level + 1, node_list)