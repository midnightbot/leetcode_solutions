##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        
        self.ans = []
        self.ok = ""
        def inorder(root):
            
            if root is not None:
                
                if root.left:
                    inorder(root.left)
                    
                if len(self.ans)!=0 and self.ans[-1] == p.val:
                    #return root.val 
                    self.ok = root
                self.ans.append(root.val)
                
                if root.right:
                    inorder(root.right)
                    
                    
        inorder(root)
        #print(self.ans,self.ok)
        if self.ok!="":
            return self.ok
        
        else:
            return None
