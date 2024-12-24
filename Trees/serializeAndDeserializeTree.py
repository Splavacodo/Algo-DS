class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []

        def preorder_traverse(node):
            if not node:
                res.append("N")
                return
            
            res.append(str(node.val))
            preorder_traverse(node.left)
            preorder_traverse(node.right)

        preorder_traverse(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        node_vals = data.split(",")

        def build_tree(index):
            if node_vals[index] == "N":
                return (None, index + 1)
            
            node = TreeNode(node_vals[index])

            index += 1
            node.left, index = build_tree(index)
            node.right, index = build_tree(index)

            return (node, index)
        
        return build_tree(0)[0]