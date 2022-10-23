import math
class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
        def find_ans(a,b):
            return math.gcd(a,b)
        
        n = len(nums)
        ans = 0
        for x in range(n):
            present = 0
            for y in range(x,n):
                present = find_ans(present,nums[y])
                if present == k:
                    ans+=1
                    
        return ans
                    
        
