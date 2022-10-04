##ss
from copy import *
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        
        for x in range(len(nums)):
            new_array = nums.copy()
            new_array.pop(x)
            ok = 0
            for y in range(len(new_array)-1):
                if new_array[y] >=new_array[y+1]:
                    ok = -1
                    
                
            if ok == 0:
                return True
        return False
