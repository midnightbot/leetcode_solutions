##ss
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        sets = set(nums)
        
        while original in sets:
            original*=2
            
        return original
        
