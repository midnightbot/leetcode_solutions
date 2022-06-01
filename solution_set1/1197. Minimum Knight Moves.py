class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        
        ## simple bfs
        ## up-, below +
        
        moves = [(+1,-2), (+2,-1), (+2,+1), (+1,+2), (-1,+2), (-2,+1), (-2,-1), (-1,-2)]
        
        
        steps = 0
        
        q = [(0,0)]
        visited = set()
        visited.add((0,0))
        while q:
            
            
            for it in range(len(q)):
                xold,yold = q.pop(0)
                
                if (xold,yold) == (x,y):
                    return steps
                
                for xa,ya in moves:
                    xt = xold + xa
                    yt = yold + ya
                    
                    if (xt,yt) not in visited:
                        q.append((xt,yt))
                        visited.add((xt,yt))
                    
            steps+=1
