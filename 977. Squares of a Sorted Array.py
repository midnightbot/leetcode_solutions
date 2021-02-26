class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        ans = [x**2 for x in nums]
        return sorted(ans)
        
