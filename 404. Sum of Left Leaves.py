# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        ans = []
        ans.append(0)
        final_ans = self.opentree(root,ans)
        return final_ans
        
        
    def opentree(self,root,ans):
        #print(ans)
        
        if root.left and not (root.left.right or root.left.left):
            ans.append(root.left.val)
            self.opentree(root.left,ans)
        elif root.left and (root.left.right or root.left.left):
            self.opentree(root.left,ans)
        
        if root.right:
            self.opentree(root.right,ans)
        print(ans)
        return sum(ans)
            

        
