##ss
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        
        ans = 0
        prev = 0
        
        for x in range(len(target)):
            ans+= max(0,target[x] - prev)
            prev = target[x]
            
        return ans
        
