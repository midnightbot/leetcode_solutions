class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:

        mods = 10**9 + 7
        ## atleast minprofit and total members in crime is at most n
        dp = [[0 for x in range(n+1)] for y in range(minProfit+1)]

        dp[0][0] = 1

        for grp,pft in zip(group, profit):
            for x in range(minProfit, -1,-1):
                for y in range(n-grp, -1,-1):
                    dp[min(x+pft, minProfit)][y+grp]+=dp[x][y]

        return sum(dp[minProfit]) % mods

