import math
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:

        score = 0

        nums = [-x for x in nums]
        heapq.heapify(nums)
        while k!=0:
            top = heapq.heappop(nums)
            top*=-1
            score+=top
            top = math.ceil(top/3)
            heapq.heappush(nums, -top)
            k-=1
        return score
