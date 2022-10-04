##Solution1 (Brute Force)
class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        
        ##non-empty continuous subarrays
        
        ans = 0
        
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                if nums[y] >= nums[x]:
                    ans+=1
                    
                else:
                    break
                    
        return ans+len(nums)
        
