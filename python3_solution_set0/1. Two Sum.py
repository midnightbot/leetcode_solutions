class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        sums = []
        for x in range(len(nums)-1):
            for y in range(x+1,len(nums)):
                if nums[x]+nums[y]==target:
                    sums.append(x)
                    sums.append(y)
                    return sums
                
        
