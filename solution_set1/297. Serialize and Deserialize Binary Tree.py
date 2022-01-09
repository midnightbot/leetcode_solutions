##ss
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.ans = ""
        if not root:
            self.ans = ""
            return self.ans
        
        self.order(root)
        #print(self.ans)
        return self.ans
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        #root.val = int(nodes[0])
        queue = [root]
        #print(type(root))
        i = 1
        while queue and i < len(nodes):
            node = queue.pop(0)
            #print(node)
            if nodes[i] != "None":
                #node 
                node.left = TreeNode(int(nodes[i]))
                queue.append(node.left)
                
            i+=1
            if nodes[i]!="None":
                node.right = TreeNode(int(nodes[i]))
                queue.append(node.right)
                
            i+=1
            
        return root
                
        
    def order(self,root):
        
        
            
        queue = [root]
        while queue:
            node = queue.pop(0)
            if not node:
                self.ans+="None,"
            else:
                self.ans+=str(node.val)+","
                queue.append(node.left)
                queue.append(node.right)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
