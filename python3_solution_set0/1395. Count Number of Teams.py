class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        dp_g, dp_l = [0] * n, [0] * n
        res = 0
        for i, r in enumerate(rating):
            for j in range(i):
                if r > rating[j]:
                    dp_g[i] += 1
                    res += dp_g[j]
                elif r < rating[j]:
                    dp_l[i] += 1
                    res += dp_l[j]
        return res
