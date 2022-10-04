##ss
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        #counter = 0
        
        while nums.count(val) > 0:
            
            nums.remove(val)
            
        return len(nums)
        
