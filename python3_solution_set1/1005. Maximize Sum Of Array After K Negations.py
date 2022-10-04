##ss
import heapq
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        
        ##
        
        
        heapq.heapify(nums)

        for x in range(k):
            top = heapq.heappop(nums)
            heapq.heappush(nums, top * -1)

        #print(nums)
        return sum(nums)
