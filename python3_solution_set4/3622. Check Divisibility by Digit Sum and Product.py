class Solution:
    def find_mul(self, n):
        temp = [int(x) for x in str(n)]
        ans = 1
        for x in temp:
            ans*=x
        return ans

    def checkDivisibility(self, n: int) -> bool:
        return n%(sum([int(x) for x in str(n)]) + self.find_mul(n)) == 0
        
