class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        ## score = sum(arr) * len(arr)
        
        ## 10**5 limits indicate for a linear solution
        
        current = 0
        ans = 0
        y = 0
        for x in range(len(nums)):
            current+=nums[x]
            
            while current * (x-y+1) >= k:
                current-=nums[y]
                y+=1
                
            ans+= x - y + 1
            
        return ans
        
