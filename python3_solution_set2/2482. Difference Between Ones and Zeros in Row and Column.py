class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:

        sums = []
        sums2 = []

        for x in grid:
            sums.append(sum(x))

        m = len(grid)
        n = len(grid[0])
        newg = [[0 for x in range(m)] for y in range(n)]

        for x in range(m):
            for y in range(n):
                newg[y][x] = grid[x][y]

        for x in newg:
            sums2.append(sum(x))

        ans = [[0 for x in range(n)] for y in range(m)]

        for x in range(m):
            for y in range(n):
                ans[x][y] = 2*sums[x] - m + 2*sums2[y] - n

        return ans
