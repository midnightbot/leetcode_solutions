##ss
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        
        ##len(nums) = n
        ## nums[i]  0<= i < n
        ## sum(nums) <= maxSum
        
        
        def check_ans(vals):
            temp2 = max(vals - index, 0)
            result = (vals + temp2) * (vals - temp2 + 1)/2
            
            temp2 = max(vals - ((n-1)-index),0)
            result+= (vals + temp2) * (vals - temp2 + 1)/2
            
            return result - vals
        
        
        maxSum-=n
        
        l = 0
        r = maxSum
        
        while l < r:
            mid = (l+r+1)//2
            
            if check_ans(mid) <= maxSum:
                l = mid
                
            else:
                r = mid - 1
                
        return l+1
                
