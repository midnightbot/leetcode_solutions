##ss
import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        ## simple binary search
        
        def can_do(thr):
            ans = 0
            for x in nums:
                ans+= math.ceil(x/thr)
                
            return ans
        
        i = 1
        j = max(nums)
        
        while i < j:
            #print(i,j)
            mid = (i+j)//2
            
            if can_do(mid) > threshold:
                i = mid + 1
                
            else:
                j = mid
                
        return i
