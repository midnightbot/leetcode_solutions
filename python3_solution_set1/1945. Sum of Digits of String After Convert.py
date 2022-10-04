##ss
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        num = ""
        
        for x in range(len(s)):
            num+= str(ord(s[x]) - ord('a') + 1)
        
        for x in range(k):
            
            sums = sum([int(x) for x in num])
            num = str(sums)
            
        return num
