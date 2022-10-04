##ss
##how to make custom sorting parameter
from functools import cmp_to_key
class Solution:
    
    
    def largestNumber(self, nums: List[int]) -> str:
        
        for x in range(len(nums)):
            nums[x] = str(nums[x])
            
        comp = lambda a, b: 1 if a + b < b + a else -1 if a + b > b + a else 0
        
        temp = ''.join(sorted(nums, key = cmp_to_key(comp)))
        return '0' if temp[0] == '0' else temp
    
        
