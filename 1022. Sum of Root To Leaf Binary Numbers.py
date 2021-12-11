##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = []
        self.dfs(root,str(root.val),ans)
        return sum(ans)
        
    def dfs(self,root,strs,ans):
        #print(root,strs)
        
        if root == None or (root.left==None and root.right==None):
            ans.append(int(strs,2))
            
        else:
            if root.left!=None:
                self.dfs(root.left,strs+str(root.left.val),ans)
                
            if root.right!=None:
                self.dfs(root.right,strs+str(root.right.val),ans)
        return ans
