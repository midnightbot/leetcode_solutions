##ss
class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        
        mins = min(nums)
        
        lens = len(nums)
        
        cons = set([mins+x for x in range(lens)])
        
        for x in nums:
            if x in cons:
                cons.remove(x)
                
        return len(cons) == 0
        
