class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        
        return nums.count(target) * 2 > len(nums)
        
