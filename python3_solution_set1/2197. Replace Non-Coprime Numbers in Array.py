##ss
import math
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        
        
        for x in range(len(nums)):
            
            stack.append(nums[x])
            
            while len(stack) >=2 and math.gcd(stack[-1],stack[-2]) > 1:
                p1 = stack.pop()
                p2 = stack.pop()

                stack.append(math.lcm(p1,p2))
                
        return stack
        
