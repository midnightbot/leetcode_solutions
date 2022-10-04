##SS
##Same as 713
##Sliding window
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        
        start = 0
        end = len(nums)
        
        ans = float('inf')
        temp = 0
        for x in range(len(nums)):
            temp+= nums[x]
            
            while temp >= target:
                ans = min(ans,x-start)  
                #ans = min(ans, x-start)
                temp-=nums[start]
                start+=1
            #print(temp,start)
                 
        if ans == float('inf'):
            return 0
        else:
            return ans+1
            
        
