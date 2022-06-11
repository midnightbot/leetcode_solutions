class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        ## as nums elements are positive
        ##as soon as some subarrays sum goes above x, it can never come back to x
        
        ## circular subarray
        
 
        pre = [0] + list(accumulate(nums))

        ans = -float('inf')
      
        
        dic = {vals:it for it,vals in enumerate(pre)}
    
        temp = pre[-1] - x
        if temp < 0:
            return -1
        
        for x in dic:
            if x + temp in dic:
                ans = max(ans, dic[x+temp] - dic[x])
                
        return len(nums) - ans if ans!= - float('inf') else -1
            
        
