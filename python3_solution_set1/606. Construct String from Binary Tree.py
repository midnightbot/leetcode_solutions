##ss
##simple recursive calls
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        self.ans = ""
        
        def expand(root):
            if root is None:
                return ""
            
            #self.ans+=str(root.val)
            a = expand(root.left)
            b = expand(root.right)
            
            temp1 = str(root.val)
            if (str(a) is not "") or (str(a) is "" and str(b) is not ""):
                temp2 = "(" + str(a) + ")"
            else:
                temp2 = ""
                
            if str(b) is not "":
                temp3 = "(" + str(b) + ")"
                
            else:
                temp3 = ""
                
            return temp1 + temp2 + temp3
        
        return expand(root)
            
        #print(self.ans)
            
        
