##ss
##similar to Q 1249
class Solution:
    def minSwaps(self, s: str) -> int:
        
        count = 0
        swaps = 0
        for x in range(len(s)):
            
            if s[x] == '[':
                count+=1
                
            elif s[x] == ']':
                count-=1
                
                if count < 0:
                    swaps+=1
                    count = 1
                    
        return swaps
        
