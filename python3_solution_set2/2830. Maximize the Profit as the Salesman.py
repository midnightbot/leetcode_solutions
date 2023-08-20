import bisect
class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:

        offers = sorted(offers, key = lambda x:x[0])
        st = [x[0] for x in offers]
        ans = 0
        ## make compatible set for each house
        compat = []
        for x,y,z in offers:
            i = bisect.bisect_left(st, y+1)
            compat.append(i)

        ## starting each index, find max solution
        nn = len(offers)
        @cache
        def solve(indx):
            if indx >= nn:
                return 0

            else:
                return max(offers[indx][2] + solve(compat[indx]), solve(indx+1))

        for i in range(0,n):
            ans = max(ans, solve(i))
        return ans
        
