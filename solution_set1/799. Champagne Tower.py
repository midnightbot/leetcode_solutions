##ss
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        ans = [[0]*x for x in range(1,102)]
        ans[0][0] = poured
        
        for x in range(query_row+1):
            for y in range(x+1):
                left = (ans[x][y] - 1) / 2
                
                if left > 0:
                    ans[x+1][y]+=left
                    ans[x+1][y+1]+=left
                    
        return min(1, ans[query_row][query_glass])
        
