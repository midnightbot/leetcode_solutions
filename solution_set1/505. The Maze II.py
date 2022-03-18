##ss
##reusing code from 499. The Maze III

import heapq
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        
        ##simple dijkstras
        q = []
        
        heapq.heappush(q,[0,start[0],start[1], ""])
        visited = set()
        
        #moves = {'d':[1,0], 'u':[-1,0], 'r':[0,1], 'l':[0,-1]}
        moves = [[1,0,'d'], [-1,0,'u'], [0,1,'r'], [0,-1,'l']]
        while q:
            
            top = heapq.heappop(q)
            
            thisdist = top[0]
            posx = top[1]
            posy = top[2]
            drn = top[3]
            
            if (posx,posy) not in visited:
                visited.add((posx,posy))
                
                
                #if [posx,posy] == destination:
                    #print(visited)
                    #return len(drn)
                
                og_x = copy.deepcopy(posx)
                og_y = copy.deepcopy(posy)
                for z in range(len(moves)):
                    c = 0
                    posx = og_x
                    posy = og_y
                    
                    while 0<=posx + moves[z][0] < len(maze) and 0<=posy+moves[z][1]<len(maze[0]) and maze[posx+moves[z][0]][posy + moves[z][1]] == 0:
                        posx+=moves[z][0]
                        posy+=moves[z][1]
                        c+=1
                        
                    if [posx,posy] == destination:
                        return len(drn) + c
                            
                            
                    if (posx,posy) not in visited:
                        heapq.heappush(q, [thisdist + c, posx, posy, drn + ''.join([str(moves[z][2]) for x in range(c)])])
                        
                    
                        
                
        
        return -1
        
