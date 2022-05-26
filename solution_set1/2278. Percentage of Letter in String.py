import math
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        
        return math.floor(len([x for x in s if x==letter])/len(s)*100)
        
        
        
