##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        ##longest seq
        ##every node can have asc and desc on 2 branches
        ##answer = (asc-chain) + (desc-chain)
        
        ans = 0
        @lru_cache(None)
        def asc(root,prev_val):##finding the maximum length ascending sequence for the current node
            if root is None:
                return 0
            elif root.val != prev_val+1:
                return 0
 
            
            elif root.val == prev_val + 1:
                return 1 + max(asc(root.left,root.val), asc(root.right,root.val))
            
        @lru_cache(None)    
        def desc(root,prev_val):##finding the maximum length descdending sequence for the current node
            
            if root is None:
                return 0
            
            elif root.val!=prev_val-1:
                return 0
            
                        
            elif root.val == prev_val -1:
                return 1 + max(desc(root.left,root.val),desc(root.right,root.val))
            
        q = [root]
        
        while q:
            
            for x in range(len(q)):
                node = q.pop(0)
                ##-1 as root node will be counted twice
                ans = max(ans, asc(node,node.val-1) + desc(node,node.val+1) - 1)
                
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
                    
        return ans
        
        
        
