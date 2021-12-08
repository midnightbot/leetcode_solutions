##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        memo = {}
        ##memo 3 info array 
        ##left tree sum, right tree sum, rootval
        finals = []
        self.sums(root,memo,finals)
        #print(finals)
        ans  = 0
        for x in range(len(finals)):
            ans+=abs(finals[x][0]-finals[x][1])
        return ans
        
        
    def sums(self,root,memo,finals):
        
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            memo[root] = [0,0,root.val]
            return root.val
        
        elif root in memo.keys():
            return memo[root][0] + memo[root][1] + memo[root][2]
        
        else:
            memo[root] = [self.sums(root.left,memo,finals),self.sums(root.right,memo,finals),root.val]
            #finals.append[memo[root][0]]
            finals.append([memo[root][0],memo[root][1]])
            return memo[root][0] + memo[root][1] + memo[root][2]
