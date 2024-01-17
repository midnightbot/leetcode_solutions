class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        temp = list(Counter(nums).values())
        maxs = max(temp)
        return temp.count(maxs) * maxs
        
        
        
