##ss
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        
        presum = [nums[0]]
        
        for x in nums[1:]:
            presum.append(presum[-1] + x)
            
        sums = sum(nums)
        
        ans = float('inf')
        indx = -1
        n = len(nums)
        
        for x in range(len(presum)):
            
            temp = abs((presum[x]//(x+1)) - ((sums-presum[x])//max((n-x-1),1)))
            
            if temp < ans:
                ans = temp
                indx = x
                
        return indx
        
