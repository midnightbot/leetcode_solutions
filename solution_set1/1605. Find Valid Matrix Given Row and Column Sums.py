##ss
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        
        ans = [[0 for x in range(len(colSum))]for y in range(len(rowSum))]
        
        #print(ans)
        
        done = [len(rowSum) + len(colSum)]
        def fill_this_row(r,val,y):
            ans[r][y] = val
            rowSum[r] = float('inf')
            colSum[y]-=val
            done[0]-=1
            if colSum[y]==0:
                colSum[y] = float('inf')
                done[0]-=1
            #done-=1
            
        def fill_this_col(c,val,x):
            ans[x][c] = val
            colSum[c] = float('inf')
            rowSum[x]-=val
            done[0]-=1
            if rowSum[x] == 0:
                rowSum[x] = float('inf')
                done[0]-=1
            #done-=1
            
        while done[0] >0:
            minr = min(rowSum)
            minc = min(colSum)
            
            indxr = rowSum.index(minr)
            indxc = colSum.index(minc)
            #print("inisde")
            if minr < minc:
                fill_this_row(indxr,minr,indxc)
                
                
            else:
                fill_this_col(indxc,minc,indxr)
                
            #done-=1
             
            #print(ans,rowSum,colSum,done)
        return ans
            
        
