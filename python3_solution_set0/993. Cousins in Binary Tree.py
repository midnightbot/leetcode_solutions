##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        ans1 = []
        ans2 = []
        temp = []
        self.expand(root,str(root.val)+",",ans1,x)
        self.expand(root,str(root.val)+",",ans2,y)
        #print(ans1,ans2)
        ##same level and differne parent
        
        indx1 = ans1[0].index(str(x))
        indx2 = ans2[0].index(str(y))
        
        if indx1 == indx2 and ans1[0][indx1-1]!=ans2[0][indx2-1]:
            return True
        else:
            return False
        
        
    def expand(self,root,strs,ans,x):
        #print(root,strs)
        
        if root.val == x:
            #print(strs)
            ans.append(strs.split(","))
            #ans = strs.split(",")
            #print(ans)
            
        else:
            if root.left!=None:
                self.expand(root.left,strs+str(root.left.val)+",",ans,x)
                
            if root.right!=None:
                self.expand(root.right,strs+str(root.right.val)+",",ans,x)
        return ans
        
