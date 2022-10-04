##ss
##simple union find
##whenever two island can combine to form new island combine them
##combining condition if new 1 inserted is neighbour of some other island
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        
        parent = {}
        count = [0]
        ans = []
        grid = [[0 for x in range(n)]for x in range(m)]
        def find_parent(x):
            #print(x)
            if x not in parent:
                #parent[x] = x
                return x
            parent[x] = find_parent(parent[x])

            return parent[x]
                
            
        def union(x,y):
            xs = find_parent(x)
            ys = find_parent(y)
            
            if xs!=ys:
                parent[ys] = xs
                count[0] = count[0]- 1
        
        for x in range(len(positions)):
            if grid[positions[x][0]][positions[x][1]] == 0:
                grid[positions[x][0]][positions[x][1]] = 1
                count[0] = count[0] + 1
                var1 = positions[x][0]
                var2 = positions[x][1]

                if var1-1>=0 and grid[var1-1][var2] == 1:
                    union(str(var1-1)+","+str(var2), str(var1)+","+str(var2))



                if var1+1 < len(grid) and grid[var1+1][var2] == 1:
                    union(str(var1+1)+","+str(var2), str(var1)+","+str(var2))



                if var2-1>=0 and grid[var1][var2-1]==1:
                    union(str(var1)+","+str(var2-1), str(var1)+","+str(var2))


                if var2+1 < len(grid[0]) and grid[var1][var2+1] == 1:
                    union(str(var1)+","+str(var2+1), str(var1)+","+str(var2))

                ans.append(count[0])
            else:    
                ans.append(count[0])
            #print(ans)
        return ans
                
                
            
