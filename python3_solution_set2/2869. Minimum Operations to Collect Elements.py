class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        nums = nums[::-1]
        ans = [x+1 for x in range(k)]
        ans = [nums.index(i) for i in ans]
        return max(ans) + 1
        
