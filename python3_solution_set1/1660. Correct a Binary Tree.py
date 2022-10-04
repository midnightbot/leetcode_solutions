##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        
        ##step1 find which value is to be removed
        ##delete that node and replace it with None
        
        q = [root]
        remove = -1
        while q:
            thislevel = set()
            for x in range(len(q)):
                
                node = q.pop(0)
                thislevel.add(node.val)
                if node.right:
                    if node.right.val in thislevel:
                        remove = node.val
                        q = []
                        break
                    
                    q.append(node.right)
                    
                if node.left:
                    q.append(node.left)
                    
            
        def remove_node(root,remove):
            
            if root is None:
                return root
            
            elif root.val == remove:
                return None
            elif root.val!=remove:
                root.left = remove_node(root.left,remove)
                root.right = remove_node(root.right,remove)
                
                return root
            
        return remove_node(root,remove)
            
            
        
