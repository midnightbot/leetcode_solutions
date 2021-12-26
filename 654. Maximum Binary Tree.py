##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        ans = self.maketree(nums)
        return ans
        
    def maketree(self,nums):
        #print(root)
        node = TreeNode()
        node.val = max(nums)
        #root.val = max(nums)
        
        indx = nums.index(max(nums))
        
        if len(nums[0:indx])!=0:
            node.left = self.maketree(nums[0:indx])
            
        if len(nums[indx+1:len(nums)])!=0:
            node.right = self.maketree(nums[indx+1:len(nums)])
        
        return node
