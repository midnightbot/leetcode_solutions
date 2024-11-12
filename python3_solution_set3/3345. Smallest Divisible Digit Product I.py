class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for x in range(n, 1000):
            temp = [int(i) for i in str(x)]
            ans = 1
            for i in temp:
                ans*=i

            if ans%t==0:
                return x
            
        
