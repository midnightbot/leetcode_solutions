##ss
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        indx = [0 for x in range(n)]
        vals = [matrix[x][0] for x in range(n)]
        
        for x in range(k):
            mins = min(vals)
            rowno = vals.index(mins)
            indx[rowno]+=1
            if indx[rowno] == n:
                vals[rowno] = float('inf')
            else:
                vals[rowno] = matrix[rowno][indx[rowno]]
            
        return mins
        
