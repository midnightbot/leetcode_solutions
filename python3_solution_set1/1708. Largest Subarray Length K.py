##ss
class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        
        maxs = max(nums[0:len(nums)-k+1])
        indx = nums.index(maxs)
        
        return nums[indx:indx+k]
        
