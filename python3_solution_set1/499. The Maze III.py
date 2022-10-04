##ss
##Solution 1 (Attemp1 , Solution is correct but does not return smallest lexical ans, it just returns some mimimum path answer)
import heapq
class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        
        #print("inside")
        ## simple dijkstras
        ##visited will be "pt[0],pt[1],drn"
        ##ans[pt[0],pt[1]]
        
        ## on wall, add pts [x+1,y] [x-1,y]  [x,y+1]  [x,y-1] -> if not visited with resp drn
        
        def makestr(pt):
            ans = ""
            
            for x in range(len(pt)):
                ans+=str(pt[x])
                
                if x != len(pt) - 1:
                    ans+=","
                    
            return ans
        
        def validpt(pt):
            
            return 0<=pt[0]<len(maze) and 0<=pt[1] < len(maze[0]) and maze[pt[0]][pt[1]] == 0
        
        q = []
        
        heapq.heappush(q,[0,ball[0],ball[1],"l"])
        heapq.heappush(q,[0,ball[0],ball[1],"r"])
        heapq.heappush(q,[0,ball[0],ball[1],"u"])
        heapq.heappush(q,[0,ball[0],ball[1],"d"])
        
        directions = {"l":[0,-1], "r":[0,1], "u":[-1,0], "d":[1,0]}
        directs = [[1,0,'d'], [-1,0,'u'], [0,1,'r'], [0,-1,'l']]
        opp = {"l":"r", "r":"l", "u":"d", "d":"u"}
        ans = {makestr([x,y]):float('inf') for x in range(len(maze)) for y in range(len(maze[0]))}
        
        movement = {makestr([x,y]):-1 for x in range(len(maze)) for y in range(len(maze[0]))}
        
        ans[makestr(ball)] = 0
    
        visited = set()
        while q:
            
            top = heapq.heappop(q)
            
            thiscost = top[0]
            posx = top[1]
            posy = top[2]
            drn = top[3]
            
            
            if makestr([posx,posy,drn]) not in visited:
                
                visited.add(makestr([posx,posy,drn]))
                #print(posx,posy,validpt([posx,posy]))
                if validpt([posx,posy]):
                    
                    newpt = [posx + directions[drn][0], posy + directions[drn][1]]
                    if validpt(newpt):
                        if ans[makestr(newpt)] > thiscost + 1:
                            ans[makestr(newpt)] = thiscost + 1
                            movement[makestr(newpt)] = opp[drn]

                            heapq.heappush(q,[thiscost+1, newpt[0],newpt[1],drn])
                        
                    else:
                        if drn == 'u' or drn == 'd':
                            ##left side
                            if makestr([posx,posy-1,"l"]) not in visited and validpt([posx,posy-1]) and ans[makestr([posx,posy-1])] > thiscost + 1:
                                ans[makestr([posx,posy-1])] = thiscost + 1
                                heapq.heappush(q,[thiscost+1, posx,posy-1, "l"])
                                movement[makestr([posx,posy-1])] = "r"
                            if makestr([posx,posy+1,"r"]) not in visited and validpt([posx,posy+1]) and ans[makestr([posx,posy+1])] > thiscost + 1:
                                ans[makestr([posx,posy+1])] = thiscost + 1
                                heapq.heappush(q,[thiscost+1, posx,posy+1, "r"])
                                movement[makestr([posx,posy+1])] = "l"
                        else:
                            if makestr([posx-1,posy,"u"]) not in visited and validpt([posx-1,posy]) and ans[makestr([posx-1,posy])] > thiscost + 1:
                                ans[makestr(posx-1,posy)] = thiscost + 1
                                heapq.heappush(q,[thiscost+1, posx-1,posy, "u"])
                                movement[makestr([posx-1,posy])] = 'd'
                            if makestr([posx+1,posy,"d"]) not in visited and validpt([posx+1,posy]) and ans[makestr([posx+1,posy])] > thiscost + 1:
                                ans[makestr([posx+1,posy])] = thiscost + 1
                                heapq.heappush(q,[thiscost+1, posx+1,posy, "d"])
                                movement[makestr([posx+1,posy])] = 'u'
                else:
                    ##we are on a wall point
                    ##go back on opp drn, we have come from here
                    ##add the rest 2 direction points
                    og_pt = [posx + directions[opp[drn]][0], posy + directions[opp[drn]][1]]
                    
                    ##l,r to be added 
                    ## or u,d to be added
                    
                    if drn == "u" or drn == 'd':
                        newpt1 = [og_pt[0] + directions["l"][0], og_pt[1] + directions["l"][1]]
                        newpt2 = [og_pt[0] + directions["r"][0], og_pt[1] + directions["r"][1]]
                        
                        if makestr(newpt1+["l"]) not in visited:
                            heapq.heappush(q,[cost, newpt1[0],newpt1[1],"l"])
                            movement[makestr(newpt1)] = "r"
                            
                        if makestr(newpt2+["r"]) not in visited:
                            heapq.heappush(q,[cost, newpt2[0],newpt2[1],"r"])
                            movement[makestr(newpt2)] = "l"
                        
                        
                    elif drn == "l" or drn == "r":
                        newpt1 = [og_pt[0] + directions["u"][0], og_pt[1] + directions["u"][1]]
                        newpt2 = [og_pt[0] + directions["d"][0], og_pt[1] + directions["d"][1]]
                        
                        
                        if makestr(newpt1+["u"]) not in visited:
                            heapq.heappush(q,[cost, newpt1[0],newpt1[1],"u"])
                            movement[makestr(newpt1)] = "d"
                        
                        if makestr(newpt2+["d"]) not in visited:
                            heapq.heappush(q,[cost, newpt2[0],newpt2[1],"d"])
                            movement[makestr(newpt2)] = "u"
                            
                            
        paths = []
        if ans[makestr(hole)] == float('inf'):
            return "impossible"
        start = hole
        #print(movement)
        result = ""
        #print(ans)
        #print(movement)
        
        while start!=ball:
            paths.append(movement[makestr(start)])
            #print(start)
            if movement[makestr(start)] == 'l':
                start = [start[0],start[1] - 1]
                
            elif movement[makestr(start)] == 'r':
                start  = [start[0],start[1] + 1]
                
            elif movement[makestr(start)] == 'u':
                start = [start[0] - 1, start[1]]
                    
                    
            else:
                start = [start[0] + 1, start[1]]
                
        
        result = ""
        prev = paths[0]
        
        for x in range(len(paths)):
            if paths[x] == prev:
                continue
                
            else:
                result+=opp[prev]
                prev = paths[x]
                
        result+=opp[prev]
        
        return result
                    
 ## Solution 2
 import heapq
class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        
        
        ##simple dijkstras
        q = []
        
        heapq.heappush(q,[0,ball[0],ball[1], ""])
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
                
                
                if [posx,posy] == hole:
                    #print(visited)
                    return drn
                
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
                        
                        if [posx,posy] == hole:
                            break
                            
                            
                    if (posx,posy) not in visited:
                        heapq.heappush(q, [thisdist + c, posx, posy, drn + str(moves[z][2])])
                        
                
        
        return "impossible"
                        
                
                
        
