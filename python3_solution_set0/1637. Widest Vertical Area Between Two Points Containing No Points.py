class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        
        ans = []
        for x in range(len(points)):
            ans.append(points[x][0])
            
        ans = sorted(ans)
        
        maxs = 0
        for x in range(len(ans)-1):
            temp = ans[x+1]-ans[x]
            if temp > maxs:
                maxs = temp
                
        return maxs
        
