class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = []
        
        for x in range(len(nums)):
            if nums[x] not in ans:
                ans.append(nums[x])
                
            else:
                ans.remove(nums[x])
                
                
        return ans
        
