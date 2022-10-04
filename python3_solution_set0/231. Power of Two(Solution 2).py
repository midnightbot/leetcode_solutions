class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n<0:
            return False
        ans = format(n,"b")
        return ans.count("1") == 1
        
        
