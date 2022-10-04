##ss
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        ##simple bfs
        
        queue = []
        visited = set()
        
        queue.append(entrance)
        
        c = 0
        while queue:
            #print(maze,"before")
            #print(queue)
            temp = len(queue)
            for x in range(temp):
                node = queue.pop(0)
                #print(node,queue)
                
                if node[0] - 1 >=0 and maze[node[0]-1][node[1]] == '.' and tuple([node[0]-1,node[1]]) not in visited and [node[0]-1,node[1]] not in queue:
                    queue.append([node[0]-1,node[1]])
                    #queue.add(tuple([node[0]-1,node[1]]))

                if node[0] + 1 < len(maze) and maze[node[0]+1][node[1]] == '.' and tuple([node[0]+1,node[1]]) not in visited and [node[0]+1,node[1]] not in queue:
                    queue.append([node[0]+1,node[1]])
                    #queue.add(tuple([node[0]+1,node[1]]))


                if node[1]-1>=0 and maze[node[0]][node[1]-1] == '.' and tuple([node[0],node[1]-1]) not in visited and [node[0],node[1]-1] not in queue:
                    queue.append([node[0],node[1]-1])
                    #queue.add(tuple([node[0],node[1]-1]))


                if node[1]+1 < len(maze[0]) and maze[node[0]][node[1]+1] == '.' and tuple([node[0],node[1]+1]) not in visited and [node[0],node[1]+1] not in queue:
                    queue.append([node[0],node[1]+1])
                    #queue.add(tuple([node[0],node[1]+1]))
                    
                    
                maze[node[0]][node[1]] = c
                visited.add(tuple(node))
            #print(maze,"after")
                
            c+=1
            
        ans = []
        
        for x in range(len(maze[0])): ##row chck
            if maze[0][x]!="+" and maze[0][x]!="." and (0!=entrance[0] or x!=entrance[1]):
                ans.append((maze[0][x],0,x))
                
                
            if maze[len(maze)-1][x]!="+" and maze[len(maze)-1][x]!="." and (len(maze)-1!=entrance[0] or x!=entrance[1]):
                ans.append((maze[len(maze)-1][x],0,x))
                
                
        for x in range(len(maze)):
            
            if maze[x][0]!="+" and maze[x][0]!="." and (x!=entrance[0] or 0!=entrance[1]):
                ans.append((maze[x][0],x,0))
                
                
            if maze[x][len(maze[0])-1]!="+" and maze[x][len(maze[0])-1]!="." and (x!=entrance[0] or len(maze[0])-1!=entrance[1]):
                ans.append((maze[x][len(maze[0])-1],x,len(maze[0])-1))
                
                
        if len(ans) == 0:
            return -1
        
        ans = sorted(ans, key = lambda x:x[0])
        return ans[0][0]
                                                                                
            
        
