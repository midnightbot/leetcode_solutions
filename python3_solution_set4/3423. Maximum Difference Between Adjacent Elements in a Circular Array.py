class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        arr = nums+nums
        ans = 0
        for x in range(1, len(arr)):
            ans = max(ans, abs(arr[x]-arr[x-1]))

        return ans
        
