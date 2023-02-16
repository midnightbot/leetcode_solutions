import math
class Solution:
    def countGoodSubsequences(self, s: str) -> int:

        @cache
        def find_comb(n,m):
            if m > n:
                return 0
            elif n == m:
                return 1
            elif m == 1:
                return n
            else:
                return ((n-m+1) * find_comb(n,m-1)//m)

        dicts = {}

        for x in s:
            dicts[x] = dicts.get(x,0) + 1

        ans = 0

        maxs = max([dicts[x] for x in dicts])
        for freq in range(1, maxs+1):
            temp = 1
            for it in dicts:
                temp*=(find_comb(dicts[it], freq)+1)
                temp%=((10**9)+7)
            temp-=1
            ans+=temp
            ans%=((10**9)+7)

        return ans%((10**9)+7)
        
