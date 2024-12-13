class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def in_order(node, node_list):
            if not node:
                return
            
            in_order(node.left, node_list)
            node_list.append(node)
            in_order(node.right, node_list)
        
        in_order_nodes = []
        in_order(root, in_order_nodes)

        return in_order_nodes[k - 1].val