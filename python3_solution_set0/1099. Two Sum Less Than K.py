##ss
##simple binary search tech
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        
        i = 0
        j = len(nums) -1 
        
        nums = sorted(nums)
        ans = -1
        while i < j:
            
            sums = nums[i] + nums[j]
            
            if sums < k:
                ans = max(ans,sums)
                i+=1
                
            else:
                j-=1
                
        return ans
                
            
        
