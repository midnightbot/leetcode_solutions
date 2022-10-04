##ss
class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        
        ##find width,height
        minx = float('inf')
        maxx = -1
        miny = float('inf')
        maxy = -1
        queue = [(x,y)]
        visited = set()
        
                    
                    
        while queue:
            for x in range(len(queue)):
                node = queue.pop(0)
                minx = min(minx,node[0])
                maxx = max(maxx,node[0])
                
                miny = min(miny,node[1])
                maxy = max(maxy,node[1])
                
                if node[0]-1>=0 and image[node[0]-1][node[1]] == '1' and (node[0]-1,node[1]) not in visited:
                    visited.add((node[0]-1,node[1]))
                    queue.append((node[0]-1,node[1]))
                    
                    
                if node[0]+1 < len(image) and image[node[0]+1][node[1]] == '1' and (node[0]+1,node[1]) not in visited:
                    visited.add((node[0]+1,node[1]))
                    queue.append((node[0]+1,node[1]))
                    
                    
                if node[1]-1>=0 and image[node[0]][node[1]-1] == '1' and (node[0],node[1]-1) not in visited:
                    visited.add((node[0],node[1]-1))
                    queue.append((node[0],node[1]-1))
                    
                    
                if node[1]+1 < len(image[0]) and image[node[0]][node[1]+1] == '1' and (node[0],node[1]+1) not in visited:
                    visited.add((node[0],node[1]+1))
                    queue.append((node[0],node[1]+1))
                    
                    
                if node[0]-1>=0 and node[1]-1>=0 and  image[node[0]-1][node[1]-1] == '1' and (node[0]-1,node[1]-1) not in visited:
                    visited.add((node[0]-1,node[1]-1))
                    queue.append((node[0]-1,node[1]-1))
                    
                    
                if node[0]-1>=0 and node[1]+1 < len(image[0]) and  image[node[0]-1][node[1]+1] == '1' and (node[0]-1,node[1]+1) not in visited:
                    visited.add((node[0]-1,node[1]+1))
                    queue.append((node[0]-1,node[1]+1))
                    
                if node[0]+1 < len(image) and node[1]-1>=0 and image[node[0]+1][node[1]-1] == '1' and (node[0]+1,node[1]-1) not in visited:
                    visited.add((node[0]+1,node[1]-1))
                    queue.append((node[0]+1,node[1]-1))
                    
                    
                if node[0]+ 1 < len(image) and node[1]+1 < len(image[0]) and image[node[0]+1][node[1]+1] == '1' and (node[0]+1,node[1]+1) not in visited:
                    visited.add((node[0]+1,node[1]+1))
                    queue.append((node[0]+1,node[1]+1))
                    
        
        if minx == maxx:
            width = 1
            
        else:
            width = (maxx-minx)+1
            
            
        if miny == maxy:
            ht = 1
            
        else:
            ht = (maxy-miny)+1
        
        return width * ht
        
