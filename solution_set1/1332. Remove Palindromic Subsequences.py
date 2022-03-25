##ss
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        
        ##min steps to make it empty
        return 0 if len(s) == 0 else(1 if s == s[::-1] else 2) 
