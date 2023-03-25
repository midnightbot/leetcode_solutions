class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        ## form rectangles and find the area

        
        ans = 0
        n = len(matrix)
        m = len(matrix[0])

        for x in range(n):
            for y in range(m):
                if matrix[x-1][y] >=1 and matrix[x][y] > 0 and x>0:
                    matrix[x][y]+=matrix[x-1][y]

            temp = sorted(matrix[x], reverse=True)
            for it in range(m):
                ans = max(ans, temp[it] * (it+1))

        return ans
       
        
