##ss
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ##from gates give dist to all other empty nodes
        queue = []
        inf = 2147483647
        for x in range(len(rooms)):
            for y in range(len(rooms[0])):
                if rooms[x][y] == 0:
                    queue.append((x,y,0))
                    
        while queue:
            for x in range(len(queue)):
                node = queue.pop(0)
                
                if node[0]-1>=0 and rooms[node[0]-1][node[1]] == inf:
                    rooms[node[0]-1][node[1]] = node[2]+1
                    queue.append((node[0]-1,node[1],node[2]+1))
                    
                if node[0]+1 < len(rooms) and rooms[node[0]+1][node[1]] == inf:
                    rooms[node[0]+1][node[1]] = node[2]+1
                    queue.append((node[0]+1,node[1],node[2]+1))
                    
                    
                if node[1]-1>=0 and rooms[node[0]][node[1]-1] == inf:
                    rooms[node[0]][node[1]-1] = node[2]+1
                    queue.append((node[0],node[1]-1,node[2]+1))
                    
                    
                if node[1]+1 < len(rooms[0]) and rooms[node[0]][node[1]+1] == inf:
                    rooms[node[0]][node[1]+1] = node[2]+1
                    queue.append((node[0],node[1]+1,node[2]+1))
        
