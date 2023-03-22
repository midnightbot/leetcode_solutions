# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if root is None:
            return "/"
        return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        nodes = data.split(',')
        self.i = 0

        def dfs():
            if self.i == len(nodes) or nodes[self.i] == '/':
                self.i+=1
                return None

            new_node = TreeNode(int(nodes[self.i]))
            self.i+=1
            new_node.left = dfs()
            new_node.right = dfs()
            return new_node

        return dfs()

        return None

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
