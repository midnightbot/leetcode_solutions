##ss
class Solution:
    def check(self, nums: List[int]) -> bool:
        
        comp = sorted(nums)
        
        for x in range(len(nums)):
            temp = nums[x:len(nums)] + nums[0:x]
            if temp == comp:
                return True
            
        return False
        
