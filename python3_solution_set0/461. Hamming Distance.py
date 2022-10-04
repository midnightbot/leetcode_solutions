class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        for z in range(31,-1,-1):
            b1 = x>>z&1
            b2 = y>>z&1
            
            ans+=not(b1==b2)
            
        return ans
