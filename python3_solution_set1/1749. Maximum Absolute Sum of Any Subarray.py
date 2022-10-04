##ss
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ##khadane algo twice
        ##once for pos sum, one for neg sum
        
        sums = 0
        maxs1 = -1
        maxs2 = -1
        
        sums2 = 0
        for x in range(len(nums)):
            sums+=nums[x]
            
            sums2+=nums[x]
            
            if sums2 <= 0:
                maxs2 = max(maxs2, -sums2)
                
            elif sums2 > 0:
                sums2 = 0
                
            if sums >= 0:
                maxs1 = max(maxs1,sums)
            elif sums < 0:
                sums = 0
                
                
        return max(maxs1,maxs2)
