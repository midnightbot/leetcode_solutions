class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        visited = set(nums)
        
        if len(visited) == len(nums):
            return False
        
        else:
            return True
        
