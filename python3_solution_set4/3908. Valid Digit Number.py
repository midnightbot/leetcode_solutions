class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        return str(n)[0]!=str(x) and str(n).count(str(x)) >= 1
        
