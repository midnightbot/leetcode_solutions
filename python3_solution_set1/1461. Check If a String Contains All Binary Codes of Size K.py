class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        temp = set()
        
        for x in range(len(s)-k+1):
            temp.add(s[x:x+k])
            
        return len(temp) == 2 ** k
        
