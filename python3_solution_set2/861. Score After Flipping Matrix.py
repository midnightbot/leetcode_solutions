class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:


        ## each iteration try making a row [111.] using col operations then find max val of that arr
        def find_max_val(grid):
            ans = 0
            for x in grid:
                a = 2**len(x)-1
                strs = "".join([str(z) for z in x])
                b = int(strs,2)
                ans+=max(b, a-b)
                #print(ans)
            return ans

        def find_maxi(grid, col):
            power = 2**col
            a = 0
            b = 0
            for x in range(len(grid)):
                if grid[x][col] == 1:
                    a+=1
                else:
                    b+=1
            #print(max(a,b)*power)
            return max(a,b)*power
            

        def conv_row(row):
            ans = []
            if row[0] == 1:
                return row[::-1]
            else:
                for x in row:
                    ans.append((x+1)%2)
            return ans[::-1]

        new_grid = []
        for x in grid:
            new_grid.append(conv_row(x))

        ans = 0
        #print(new_grid)
        for x in range(len(grid[0])):
            ans+=find_maxi(new_grid, x)

        return ans
