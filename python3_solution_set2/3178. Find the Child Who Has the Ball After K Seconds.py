class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        ans = k % (2*n-2)
        return ans if ans < n else 2*n-2-ans
        
