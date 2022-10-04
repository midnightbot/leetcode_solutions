class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        
        ans = [[0 for x in range(len(mat[0]))]for y in range(len(mat))]
        
        #print(ans)
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                
                temp = 0
                for r in range(max(0,x-k),min(x+k+1,len(mat))):
                    for c in range(max(0,y-k),min(y+k+1,len(mat[0]))):
                        temp+=mat[r][c]
                        
                ans[x][y] = temp
                
                
        return ans
        
