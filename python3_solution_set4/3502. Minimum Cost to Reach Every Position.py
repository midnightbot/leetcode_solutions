class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        ans = []

        for x in range(len(cost)):
            if x==0:
                ans.append(cost[x])
            else:
                ans.append(min(ans[-1], cost[x]))
        return ans
        
