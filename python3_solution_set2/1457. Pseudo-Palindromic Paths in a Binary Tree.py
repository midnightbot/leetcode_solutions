# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        ans = [0]
        
        def find_ans(root, freq):
            if root.left is None and root.right is None:
                if root.val in freq:
                    freq.remove(root.val)
                    if len(freq) <=1:
                        ans[0]+=1
                    freq.add(root.val)
                else:
                    freq.add(root.val)
                    if len(freq) <=1:
                        ans[0]+=1
                    freq.remove(root.val)
                    
            else:
                if root.val not in freq:
                    freq.add(root.val)
                    
                    if root.left:
                        find_ans(root.left, freq)
                    if root.right:
                        find_ans(root.right, freq)
                        
                    freq.remove(root.val)
                    
                else:
                    freq.remove(root.val)
                    if root.left:
                        find_ans(root.left, freq)
                    if root.right:
                        find_ans(root.right, freq)
                        
                    freq.add(root.val)
                    
        find_ans(root, set())
        return ans[0]
        
