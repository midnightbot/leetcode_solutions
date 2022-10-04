##ss
import heapq
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        
        ##operation -> for any x nums[x] = nums[x] / 2
        
        ##no. of operations to reduce sum by atleast half
        
        sums = sum(nums)
        
        reduce = 0
        steps = 0 
        q = []
        for x in nums:
            heapq.heappush(q,-x)
            
        while reduce*2 < sums:
            steps+=1
            
            top = heapq.heappop(q)
            top = top*-1
            
            reduce+=top/2
            heapq.heappush(q,-top/2)
            
        return steps
            
        
