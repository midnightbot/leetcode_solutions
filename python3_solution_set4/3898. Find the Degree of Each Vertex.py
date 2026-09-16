class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        degree = {}

        n = len(matrix)
        for x in range(n):
            degree[x] = 0

        for x in range(n):
            for y in range(n):
                if matrix[x][y] == 1:
                    degree[x]+=1
                    degree[y]+=1
        
        ans = []
        for x in range(n):
            ans.append(degree[x]//2)
        return ans
