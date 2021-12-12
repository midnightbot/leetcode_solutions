##ss
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        
        gaps = k
        
        i = 0
        j = 1
        
        while i<j and j < len(nums):
            if nums[j] - nums[i] > gaps:
                return nums[i] + gaps
            else:
                gaps-=(nums[j]-nums[i]-1)
                i+=1
                j+=1
                
        return nums[len(nums)-1] + gaps
        
