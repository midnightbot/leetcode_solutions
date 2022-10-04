##ss
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        pos = []
        neg = []
        
        for x in range(len(nums)):
            
            if nums[x] >0:
                pos.append(nums[x])
                
            else:
                neg.append(nums[x])
                
                
        result = []
        
        for x in range(len(pos)):
            result.append(pos[x])
            result.append(neg[x])
            
        return result
        
        
