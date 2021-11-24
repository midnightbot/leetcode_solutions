class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        ans  = 0
        
        for x in range(len(colors)):
            for y in range(len(colors)-1,x,-1):
                if colors[x]!=colors[y]:
                    ans = max(ans,abs(y-x))
                    break
        return ans
        
