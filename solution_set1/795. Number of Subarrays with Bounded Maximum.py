##ss
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        
        result = 0
        ans1 = 0
        ans2 = 0
        temp = 0
        for x in range(len(nums)):
            if nums[x] <= right:
                temp+=1
                
            else:
                temp = 0
            ans1+=temp
            
        temp = 0
        for x in range(len(nums)):
            if nums[x] <= left - 1:
                temp+=1
            else:
                temp = 0
                
            ans2+=temp
            
        return ans1 - ans2
                
        
