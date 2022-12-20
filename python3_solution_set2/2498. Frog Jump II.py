class Solution:
    def maxJump(self, stones: List[int]) -> int:
        if len(stones) == 2:
            return stones[-1] - stones[0]
        ans = -1
        for x in range(len(stones)-2):
            ans = max(ans, stones[x+2] - stones[x])

        return ans
