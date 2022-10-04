##ss
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        
        ans = []
        
        for x in range(len(rectangles)):
            ans.append(min(rectangles[x][0],rectangles[x][1]))
            
        return ans.count(max(ans))
        
