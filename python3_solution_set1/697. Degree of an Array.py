##ss
import collections
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        frequency = collections.Counter(nums)
        frequency = dict(frequency)
        
        high_freq = []
        
        highest = max(frequency.values())
        for x in frequency.keys():
            if frequency[x] == highest:
                high_freq.append(self.lens(nums,x))
                
        return min(high_freq)
                
        
    def lens(self,nums,this):
        f = 0
        l = 0
        for x in range(len(nums)):
            if nums[x] == this:
                f = x
                break
                
        for x in range(len(nums)-1,-1,-1):
            if nums[x] == this:
                l = x
                break
                
        return (l-f)+1
        
