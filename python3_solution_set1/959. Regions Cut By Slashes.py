##ss
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        
        ##/ or \ or blank
        ##\\  or  /    or blank
        
        parent = {}
        
        def find_parent(x):
            if x not in parent:
                return x
            parent[x] = find_parent(parent[x])
            return parent[x]
        
        def union(x,y):
            xs = find_parent(x)
            ys = find_parent(y)
            
            if xs!=ys:
                parent[ys] = xs
                return True
            
            return False
        
        
        """
        square divided into 4 parts, draw the 2 diagonals, those are the 4 parts (4 triangles)
         ________
        |   p3  | 
        |p0   p2|
        |___p1__|       
         
        """
        
        
        for x in range(len(grid)):
            for y in range(len(grid)):
                
                if y!=0:
                    c1 = str(x) +","+ str(y-1)+ ","+ str(2)
                    c2 = str(x) + ","+str(y) + ","+str(0)
                    union(c1,c2)
                    
                if x!=0:
                    c1 = str(x-1) + ","+str(y)+"," + str(1)
                    c2 = str(x) + ","+str(y) + ","+str(3)
                    union(c1,c2)
                    
                c = str(x) + ","+str(y)    
                if grid[x][y] != '/':
                    
                    union(c+","+str(3), c+","+str(2))
                    union(c+","+str(0), c+","+str(1))
                    
                if grid[x][y] != '\\':
                    union(c+","+str(0), c+','+str(3))
                    union(c+","+str(1), c+","+str(2))
                    
                    
                    
        grps = set()
        
        for x in parent:
            grps.add(find_parent(x))
            
        return len(grps)
        
        
