##ss
class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        
        ## wall, floor or box
        ##up,down,left,right
        
        ##basically bfs from box to target but the direction in which box is pushed opp direction adj cell must be epmty for the person to stand
        ##therefore 2 bfs, one for box, second to find if person can move to corresponding pos to push the box
        
        ## (posx, posy,entering direction) to be noted for visited
        ## (0,0,'l') (0,0,'r') (0,0,'u') (0,0,'d')
        
        #for x in range(len(grid)):
            #print(grid[x])
            
        boxpos = []
        target = []
        player = []
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 'B':
                    boxpos = (x,y)
                    
                if grid[x][y] == 'T':
                    target = (x,y)
                    
                if grid[x][y] == 'S':
                    player = (x,y)
        ## moves, posx, posy
        
        ##can go from p1->p2
        @lru_cache(None)
        def personbfs(p1,p2,boxpos):
            q = [copy.deepcopy(p1)]
            vis = set()
            
            if p1 == p2:
                return True
            
            while q:
                top = q.pop(0)
                x = top[0]
                y = top[1]
                
                if top not in vis:
                    vis.add(top)
                    
                    if top == p2:
                        return True
                    
                    for moves in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                        if moves not in vis and 0<=moves[0] < len(grid) and 0<= moves[1] < len(grid[0]) and (grid[moves[0]][moves[1]] != '#') and moves!=boxpos:
                            q.append(moves)
                            
                            
                        
                    
            return False
        
        def isvalidpt(p1):
            return 0<=p1[0]<len(grid) and 0<=p1[1]<len(grid[0])
        
        q = [(0,boxpos[0],boxpos[1],player[0],player[1])]
        visited = set()
        visited.add((boxpos[0],boxpos[1],"n"))
        #print(personbfs((2,2),(2,1)))
        while q:
            #print(q)
            top = q.pop(0)
            dist = top[0]
            posx = top[1]
            posy = top[2]
            
            ppx = top[3]
            ppy = top[4]
            #print(posx,posy,ppx,ppy)
            if (posx,posy) == target:
                #print("inside")
                return dist
            
            
            #zvisited.add((posx,posy))

            if (posx-1,posy,"d") not in visited and isvalidpt((posx-1,posy)) and grid[posx-1][posy] != '#':
                if personbfs((ppx,ppy),(posx+1,posy),(posx,posy)):
                    visited.add((posx-1,posy,"d"))
                    q.append((dist+1,posx-1,posy,posx,posy))

            if (posx+1,posy,"u") not in visited and isvalidpt((posx+1,posy)) and  grid[posx+1][posy] !="#":
                if personbfs((ppx,ppy),(posx-1,posy),(posx,posy)):
                    visited.add((posx-1,posy,"u"))
                    q.append((dist+1,posx+1,posy,posx,posy))

            if (posx,posy-1,"r") not in visited and isvalidpt((posx,posy-1)) and  grid[posx][posy-1] != '#':
                if personbfs((ppx,ppy),(posx,posy+1),(posx,posy)):
                    visited.add((posx,posy-1,'r'))
                    q.append((dist+1,posx,posy-1,posx,posy))

            if (posx,posy+1,'l') not in visited and isvalidpt((posx,posy+1)) and grid[posx][posy+1] != '#':
                if personbfs((ppx,ppy), (posx,posy-1),(posx,posy)):
                    visited.add((posx,posy+1,'l'))
                    q.append((dist+1,posx,posy+1,posx,posy))
                    
        
        
        return -1
        #print(visited)
        
        
        
        
        
