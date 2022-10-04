##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        maxans = root.val
        thislevel = 1
        
        q = [root]
        c = 0
        while q:
            thisans = 0
            c+=1
            for x in range(len(q)):
                node = q.pop(0)
                thisans+=node.val
                
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
                    
            if thisans > maxans:
                maxans = thisans 
                thislevel = c
                
        return thislevel
                    
                    
            
        
