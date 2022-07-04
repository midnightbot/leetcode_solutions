class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        ## children with higher rating more candies than neighbors
        n = len(ratings)
        ans = [1 for x in range(n)]
        
        for x in range(n-1):
            if ratings[x] < ratings[x+1]:
                ans[x+1] = max(ans[x+1], 1 + ans[x])
                
                
        for x in range(n-2,-1,-1):
            if ratings[x+1] < ratings[x]:
                ans[x] = max(ans[x], 1 + ans[x+1])
            
        
        return sum(ans)
