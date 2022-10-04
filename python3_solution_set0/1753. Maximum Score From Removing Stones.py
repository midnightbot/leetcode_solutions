##ss
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        
        temp = [a,b,c]
        temp = sorted(temp)
        
        return min((a+b+c)//2, temp[0] + temp[1])
        
        
        
        
