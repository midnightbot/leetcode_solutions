from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        q = deque([(0,0)])
        ans = float('inf')
        curr = 0

        for x in range(len(nums)):
            curr += nums[x]

            while q and curr - q[0][1] >= k:
                ans = min(ans, x - q.popleft()[0] + 1)

            while q and curr <= q[-1][1]:
                q.pop()

            q.append((x+1, curr))

        return ans if ans!=float('inf') else -1
        
