from collections import deque

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
        preorder = []
        self.get_preorder(root, preorder)

        inorder = []
        self.get_inorder(root, inorder)

        serialized_tree = "a" + ",".join(map(str, preorder)) + "b" + ",".join(map(str, inorder))
        return serialized_tree

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # Find the start of preorder and inorder segments
        preorder_data = data[data.index("a") + 1 : data.index("b")]
        inorder_data = data[data.index("b") + 1 :]

        # Split and filter out empty strings
        preorder = [int(x) for x in preorder_data.split(",") if x]
        inorder = [int(x) for x in inorder_data.split(",") if x]
        
        return self.buildTree(preorder, inorder)
        
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        print(preorder)
        print(inorder)
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

    def get_preorder(self, node, node_list):
        if not node:
            return
        
        node_list.append(node.val)
        self.get_preorder(node.left, node_list)
        self.get_preorder(node.right, node_list)

    def get_inorder(self, node, node_list):
        if not node:
            return
        
        self.get_inorder(node.left, node_list)
        node_list.append(node.val)
        self.get_inorder(node.right, node_list)