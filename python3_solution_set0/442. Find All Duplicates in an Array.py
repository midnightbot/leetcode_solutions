class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        ans = []
        
        
        for x in nums:
            nums[abs(x)-1] = - nums[abs(x)-1]
            
            if nums[abs(x)-1]>=0:
                ans.append(abs(x))
                
        return ans
        
