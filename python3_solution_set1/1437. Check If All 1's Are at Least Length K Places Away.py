##ss
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        
        
        prev = -1
        
        for x in range(len(nums)):
            if nums[x] == 1 and prev == -1:
                prev = x
                
            elif nums[x] == 1 and prev!=-1:
                dist = x - prev - 1
                prev = x
                if dist < k:
                    return False
                
        return True
        
