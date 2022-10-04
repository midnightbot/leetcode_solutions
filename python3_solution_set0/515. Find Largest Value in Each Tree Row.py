# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []
        if root == None:
            return []
        current_level = [root]
        next_level = []
        ans.append(root.val)
        while len(current_level)!=0:
            temp = []
            for x in current_level:
                
                if x.left:
                    temp.append(x.left.val)
                    next_level.append(x.left)
                    
                if x.right:
                    temp.append(x.right.val)
                    next_level.append(x.right)
                    
            
            if len(temp)!=0:
                maxs = max(temp)
                ans.append(maxs)
            
            current_level = next_level
            next_level = []
            
        return ans
        
