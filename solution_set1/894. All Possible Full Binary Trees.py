##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @lru_cache()
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        if not n :
            return []
        if n == 1:
            return [TreeNode(0)]
        
        temp = []
        
        for x in range(n):
            for left in self.allPossibleFBT(x):
                for right in self.allPossibleFBT(n-x-1):
                    temp.append(TreeNode(0,left,right))
                    
        return temp
        
