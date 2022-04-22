##ss
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        ans = 0
        
        l = 0
        r = len(nums) - 1
        mods = 10**9 + 7
        
        while l <= r:
            if nums[l] + nums[r] > target:
                r-=1
                
            else:
                ans+= pow(2,r-l,mods)
                l+=1
                
        return ans%mods
                
                
        
