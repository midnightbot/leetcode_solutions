##ss
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        for x in range(1,len(nums)):
            if nums[x] < nums[x-1]:
                return nums[x]

        
        return nums[0]
        
