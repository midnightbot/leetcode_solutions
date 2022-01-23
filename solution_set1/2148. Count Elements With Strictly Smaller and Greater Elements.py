##ss
class Solution:
    def countElements(self, nums: List[int]) -> int:
        
        mins = nums.count(min(nums))
        maxs = nums.count(max(nums))
        
        if mins!=len(nums):
            return len(nums) - mins - maxs
        
        else:
            return 0
        
