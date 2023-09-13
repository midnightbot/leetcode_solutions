class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0

        for x in range(low,high+1):
            if len(str(x))%2==0:
                n = len(str(x))
                a = [int(i) for i in str(x)[:n//2]]
                b = [int(i) for i in str(x)[n//2:]]
                if sum(a) == sum(b):
                    ans+=1
        return ans
        
