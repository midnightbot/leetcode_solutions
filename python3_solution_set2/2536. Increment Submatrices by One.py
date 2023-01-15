class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:

        ## simple line sweep

        mat = [[0 for x in range(n)]for y in range(n)]

        for r1,c1,r2,c2 in queries:
            for r in range(r1,r2+1):
                mat[r][c1]+=1
                if c2+1 < n:
                    mat[r][c2+1]-=1

        for x in range(n):
            for y in range(1,n):
                mat[x][y]+=mat[x][y-1]
        return mat
