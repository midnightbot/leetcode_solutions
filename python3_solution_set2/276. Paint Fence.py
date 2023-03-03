class Solution:
    def numWays(self, n: int, k: int) -> int:

        ## upto two fences with same color
        if n == 1:
            return k

        same = [0 for x in range(n+1)]
        diff = [0 for x in range(n+1)]

        same[0] = 0
        same[1] = 0
        same[2] = k 

        diff[1] = k
        diff[2] = k * (k-1)

        for x in range(3,n+1):
            same[x] = diff[x-1]
            diff[x] = (same[x-1] + diff[x-1]) * (k-1)

        return same[-1] + diff[-1]
