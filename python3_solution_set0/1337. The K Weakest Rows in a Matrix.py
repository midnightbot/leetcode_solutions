##ss
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        ans = []
        
        for x in range(len(mat)):
            var = False
            for y in range(len(mat[0])):
                if mat[x][y] == 0:
                    ans.append((y,x))
                    var = True
                    break
                    
            if var == False:
                ans.append((y+1,x))
                    
            
            
            
        ans = sorted(ans, key = lambda x:x[0])
        final = []
        
        for x in range(k):
            final.append(ans[x][1])
            
        return final
        
