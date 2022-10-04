##ss
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        
        ans = 0
        
        x = 0
        if len(nums) == 1:
            return nums[0]
        while x < len(nums):
            for y in range(x+1,len(nums)):
                if nums[y] <= nums[y-1]:
                    break
                    
            #print(nums[x:y])
            if y!=len(nums)-1 :
                ans = max(ans,sum(nums[x:y]))
            
                x+=(y-x)
            elif y==len(nums)-1 and nums[len(nums)-1] > nums[len(nums)-2]:
                ans = max(ans,sum(nums[x:y+1]))
            
                x+=(y-x) + 1
                
            elif y==len(nums)-1 and nums[len(nums)-1] <= nums[len(nums)-2]:
                ans = max(ans,sum(nums[x:y]))
            
                x+=(y-x) + 1

        return ans
        
