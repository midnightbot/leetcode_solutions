class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        return sum([int(x)**2 for x in str(n)]) - sum([int(x) for x in str(n)]) >= 50
        
