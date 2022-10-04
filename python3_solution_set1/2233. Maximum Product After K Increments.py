##ss
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        
        mods = 10**9 + 7
        
        
        
        heapq.heapify(nums)
        
        for x in range(k):
            top = heapq.heappop(nums)
            heapq.heappush(nums,top+1)
            
        result = 1
        
        for x in nums:
            result*=x
            result%= mods
            
        return result
        
