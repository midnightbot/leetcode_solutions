##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if self.areequal(root,subRoot):
            return True
        
        else:
            queue =  [root]
            while queue:
                #print(queue)
                node = queue.pop(0)
                #print(node == subRoot,node,subRoot)
                if self.areequal(node,subRoot):
                    #print("hi")
                    return True
                if node.left!=None:
                    queue.append(node.left)
                    
                if node.right!=None:
                    queue.append(node.right)
                    
                    
        return False
                    
    def areequal(self,root,subRoot):
        if root is None and subRoot is None:
            return True
        
        if root is not None and subRoot is not None:
            return (root.val == subRoot.val and self.areequal(root.left,subRoot.left) and self.areequal(root.right,subRoot.right))
        
        
        
        
        
        
