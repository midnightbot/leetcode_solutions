##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        ans = []
        strs = 1
        t = self.see(root,strs,ans)
        return max(ans)
    
    def see(self,root,strs,ans):
        
        if root == None or(root.left == None and root.right == None):
            #temp = max(temp,strs)
            #ans = max(ans,strs)
            ans.append(strs)
            #print(ans)
            
        else:
            if root.left:
                self.see(root.left,strs+1,ans)
                
            if root.right:
                self.see(root.right,strs+1,ans)
        
        #return temp
