##ss
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        
        ## return min steps to acquire all keys
        ## we can do simple bfs, whichever combination results the best ans return that
        
        ans = float('inf')
        

        pos = -1
        all_keys = [0 for x in range(6)]
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '@':
                    pos = (x,y)
                    
                if grid[x][y] in ['.', '#']:
                    continue
                    
                if 0<=ord(grid[x][y]) - ord('a') < 6:
                    
                    all_keys[ord(grid[x][y]) - ord('a')] = 1
                    
                
        
        all_keys = tuple(all_keys)
        #print(all_keys)
        q = [(pos[0],pos[1],tuple([0] * 6))]
        visited = set()
        visited.add((pos[0],pos[1],tuple([0] * 6)))
        
        moves = 0
        while q:
            for x in range(len(q)):
                top = q.pop(0)
                x = top[0]
                y = top[1]
                keys = top[2]

                for a,b in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                    if 0<=a<len(grid) and 0<=b<len(grid[0]) and grid[a][b]!='#':
                        if grid[a][b] == '.' or grid[a][b] == '@':
                            if (a,b,keys) not in visited:
                                q.append((a,b,keys))
                                visited.add((a,b,keys))
                                
                            
                        elif grid[a][b].islower():
                            newk = list(keys)
                            newk[ord(grid[a][b]) - ord('a')] = 1
                            newk = tuple(newk)
                            
                            if newk == all_keys:
                                return moves+1
                            
                            if (a,b,newk) not in visited:
                                q.append((a,b,newk))
                                visited.add((a,b,newk))
                                
                        else:
                            #print(ord(grid[a][b].lower()) - ord('a'),grid[x][y])
                            if keys[ord(grid[a][b].lower()) - ord('a')] == 1 and (a,b,keys) not in visited:
                                q.append((a,b,keys))
                                visited.add((a,b,keys))
                                
            moves+=1
                            
        return -1
        
        
