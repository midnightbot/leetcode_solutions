import math
import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        q = []

        for x in gifts:
            heapq.heappush(q, -x)

        while q and k!=0:
            top = heapq.heappop(q)
            top = top*-1

            sq = math.floor(math.sqrt(top))

            heapq.heappush(q, -sq)
            k-=1

        return -sum(q)
