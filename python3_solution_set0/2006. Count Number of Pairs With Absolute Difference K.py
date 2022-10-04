class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        
        ans  = 0
        
        for x in range(len(nums)-1):
            for y in range(x+1,len(nums)):
                if abs(nums[y]-nums[x]) == k:
                    ans+=1
                    
        return ans
        
