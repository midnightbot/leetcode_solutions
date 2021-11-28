class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        nums = sorted(nums)
        ans  = []
        for x in range(len(nums)):
            if nums[x] == target:
                ans.append(x)
                
        return ans
        
