import itertools
class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        arr = [x for x in range(len(mat[0]))]
        temp = list(itertools.combinations(arr, cols))
        ans = -1
        
        g = {x:set() for x in range(len(mat))}
        
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                if (mat[x][y] == 1):
                    g[x].add(y)
        
        def find_ans(arr):
            cov = 0
            seen = set()
            for x in arr:
                seen.add(x)
                
            for x in g:
                done = True
                for y in g[x]:
                    if y not in seen:
                        done = False
                        break
                if done == True:
                    cov+=1
            return cov
        
        for x in temp:
            ans = max(ans, find_ans(x))
            
        return ans
