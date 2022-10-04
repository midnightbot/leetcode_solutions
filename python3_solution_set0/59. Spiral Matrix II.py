##ss
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        ans = [[0 for x in range(n)] for y in range(n)]
        print(ans)
        val = 1
        for x in range((n+1)//2):
            
            
            for y in range(0+x,len(ans)-x):
                ans[x][y] = val
                val+=1
                
            for y in range(0+x+1,len(ans)-x):
                ans[y][len(ans)-x-1] = val
                val+=1
                
            for y in range(len(ans)-2-x,-1+x,-1):
                ans[len(ans)-x-1][y] = val
                val+=1
                
            for y in range(len(ans)-2-x,x,-1):
                ans[y][x] = val
                val+=1
                
        return ans
