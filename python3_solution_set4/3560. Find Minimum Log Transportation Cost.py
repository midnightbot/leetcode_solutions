class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        return max(n - k, m - k, 0) * k
        
