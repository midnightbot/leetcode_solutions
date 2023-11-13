class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0

        for x in range(0, min(n, limit)+1):
            for y in range(0, min(n-x, limit) + 1):
                c1 = x
                c2 = y
                c3 = n - x - y
                if c3 <= limit:
                    ans+=1
        return ans
        
