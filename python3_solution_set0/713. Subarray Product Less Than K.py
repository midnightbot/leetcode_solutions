##ss good basic question
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        if k <= 1:
            return 0
        ans = 0
        
        left = 0
        product = 1
        for x in range(0,len(nums)):
            product*=nums[x]
            
            while product >= k:
                
                product /= nums[left]
                left+=1
                
            ans+=x-left+1
            
        return ans
                
        
        
        
