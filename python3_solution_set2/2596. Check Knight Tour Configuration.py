class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:

        n = len(grid)
        m = len(grid[0])

        g = {}

        for x in range(n):
            for y in range(m):
                g[grid[x][y]] = (x,y)

        def is_valid(x,y):
            return 0<=x<n and 0<=y<m

        def generate_moves(x,y):
            temp = [[x+1,y+2], [x+2,y+1], [x+2,y-1], [x+1,y-2], [x-1,y+2], [x-2,y+1], [x-2, y-1], [x-1, y-2]]

            ans = set()
            for new_x, new_y in temp:
                if is_valid(new_x, new_y):
                    ans.add((new_x,new_y))

            return ans
            

        curr_x = 0
        curr_y = 0
        curr_num = 0
        #print(g)
        while curr_num!=(n*n)-1:
            #curr_num+=1
            to_go = curr_num+1
            neis = generate_moves(curr_x, curr_y)
            #print(neis, curr_x, curr_y)
            if g[to_go] in neis:
                curr_num+=1
                curr_x = g[to_go][0]
                curr_y = g[to_go][1]
            else:
                return False

            #print(curr_num)
        return True


