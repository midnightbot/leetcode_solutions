
##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        ##root to leaf
        
        #visited = set()
        ##simple dfs, explore all paths and see if it can form a palindrome
        ##a given string can be converted into a palindrome if it has zero or one character with odd freq
        
        self.ans = 0
        def expand(root,visited):
            if root is None:
                return
            
                
            if root.val in visited:
                visited.remove(root.val)
            else:
                visited.add(root.val)
            
            
            if root.left == None and root.right == None:
                if len(visited) <= 1:
                    self.ans+=1
            
            
            expand(root.left,copy.deepcopy(visited))
            expand(root.right,copy.deepcopy(visited))
        
        expand(root,set())
        return self.ans
