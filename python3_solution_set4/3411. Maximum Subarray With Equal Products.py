import math
from functools import reduce
import operator
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ans = 0
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                arr = nums[x:y+1]
                if math.gcd(*arr) * math.lcm(*arr) == reduce(operator.mul, arr):
                    ans = max(ans, y-x+1)
        return ans
        
