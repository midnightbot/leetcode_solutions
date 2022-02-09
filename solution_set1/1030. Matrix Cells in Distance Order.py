##ss
class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        
        ans = []
        
        for x in range(rows):
            for y in range(cols):
                ans.append((abs(x-rCenter) + abs(y-cCenter),x,y))
        
        
        ans = sorted(ans, key = lambda x:x[0])
        ans = [[ans[x][1],ans[x][2]] for x in range(len(ans))]
        
        return ans
        
