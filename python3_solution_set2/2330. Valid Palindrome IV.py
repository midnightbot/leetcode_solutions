##ss
class Solution:
    def makePalindrome(self, s: str) -> bool:
        
        return sum([s[x]!=s[-1-x] for x in range(len(s)//2)]) <= 2
        
