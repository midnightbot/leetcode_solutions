class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:

        dp = {0:0}

        for x in rods:
            new_dp = dp.copy()
            for diff, rod2 in dp.items():
                new_dp[diff + x] = max(new_dp.get(x + diff, 0), rod2)
                new_dp[abs(diff - x)] = max(new_dp.get(abs(diff-x), 0), rod2 + min(diff, x))
            dp = new_dp
            

        return dp[0]
        
