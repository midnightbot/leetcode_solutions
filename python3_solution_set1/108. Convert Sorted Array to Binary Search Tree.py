##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        self.n = len(nums)
        return self.maketree(nums)
        
        
    def maketree(self,nums):
            
        if len(nums) == 0:
            return None
        else:
            l = 0
            r = len(nums) - 1
            mid = l + (r-l)//2

            newnode = TreeNode()
            newnode.val = nums[mid]
            newnode.left = self.maketree(nums[0:mid])
            newnode.right = self.maketree(nums[mid+1:])

            return newnode
        
