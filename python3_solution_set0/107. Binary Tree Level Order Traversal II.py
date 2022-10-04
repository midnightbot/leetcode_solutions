# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None:
            return []
        
        
        this_level = [root]
        next_level = []
        
        temp = []
        ans = []
        ans.append([root.val])
        while len(this_level)!=0: ## checking if this level has nodes to be explored
            temp = []
            for x in this_level: ##exploring all nodes of this level
                ## so we can add all next level nodes in one list and append in the ans
                
                if x.left:
                    temp.append(x.left.val)
                    next_level.append(x.left)
                    
                if x.right:
                    temp.append(x.right.val)
                    next_level.append(x.right)
                    
            ans.append(temp)
            
            this_level = next_level
            
            next_level = []
            
        ans = ans[::-1]
        return (ans[1:len(ans)])
