##ss
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        while len(nums)!=1:
            
            arr = []
            
            for x in range(len(nums)-1):
                arr.append((nums[x] + nums[x+1])%10)
                
            nums = arr
            
        return nums[0]
                
        
