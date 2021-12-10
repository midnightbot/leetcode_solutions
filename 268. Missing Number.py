##ss
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        
        
        ans = [-1 for x in range(len(nums)+1)]
        print(ans)
        
        for x in range(len(nums)):
            ans[nums[x]] = nums[x]
            
        return ans.index(-1)
        
