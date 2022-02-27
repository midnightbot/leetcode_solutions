##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        if root is None:
            return 0
        ans = 0
        q = [[root, [0]]]
        
        while q:
            for x in range(len(q)):
                node = q.pop(0)
                
                opts = []
                for z in node[1]:
                    newv = z + node[0].val
                    if newv == targetSum:
                        ans+=1
                    opts.append(newv)
                    
                opts.append(0)
                
                if node[0].left:
                    q.append([node[0].left,opts])
                if node[0].right:
                    q.append([node[0].right, opts])
        
        
        return ans
