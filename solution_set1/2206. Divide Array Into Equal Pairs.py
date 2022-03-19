##ss
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        cnt = set()
        
        for x in nums:
            if x in cnt:
                cnt.remove(x)
                
            else:
                cnt.add(x)
                
        return len(cnt) == 0
        
