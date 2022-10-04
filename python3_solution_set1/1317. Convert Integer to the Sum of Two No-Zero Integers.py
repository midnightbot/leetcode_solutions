##ss
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        
        def non_zero(nums):
            
            return str(nums).count('0') == 0
        
        
        for x in range(1,n+1):
            if non_zero(x) and non_zero(n-x):
                return [x,n-x]
        
