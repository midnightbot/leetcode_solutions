class Solution:
    def maxProduct(self, n: int) -> int:
        arr = sorted([int(x) for x in str(n)])
        return arr[-1]*arr[-2]
        
