##ss
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        mins = min(nums)
        maxs = max(nums)
        
        ans = 1
        for x in range(1,min(maxs,mins)+1):
            if mins%x==0 and maxs%x==0:
                ans = x
                
        return ans
        
