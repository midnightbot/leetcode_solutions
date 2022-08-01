class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        if k == len(nums):
            return sum(nums)/len(nums)
        ans = -float('inf')
        pre = [0]
        for x in nums:
            pre.append(pre[-1]+x)
               
        for x in range(len(nums)-k+1):
            ans = max(ans, pre[x+k]-pre[x])
        return ans/k
    
    
