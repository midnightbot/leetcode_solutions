# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
##ss
## simple recursion
import math
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        ## [sum of subtree, num of nodes]
        ## required for every node then do weighted avearage
        
        self.ans = 0
        
        def find_ans(root):
            
            if root is None:
                return 0,0
            
            else:
                temp1 = 0
                temp2 = 0
                if root.left:
                    
                    nextans = find_ans(root.left)
                    
                    temp1+=root.left.val + nextans[0]
                    temp2+=1 + nextans[1]
                    
                    
                
                if root.right:
                    nextans = find_ans(root.right)
                    
                    temp1+=root.right.val + nextans[0]
                    temp2+=1 + nextans[1]
                    
                if root.val == math.floor((temp1+root.val) / (temp2+1)):
                    self.ans+=1
                    #print("ans",root)
                #print(temp1,temp2+1,root)
                return temp1,temp2
            
        
        find_ans(root)
        return self.ans
