#ss
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        #pseudocode
        ##add all zeros to bfs queue
        ##run bfs from all these and update dist of 1
        
        queue = []
        
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                if mat[x][y] == 0:
                    queue.append((x,y))
                    
                else:
                    mat[x][y] = -1
            
        c = 0
        while queue:
            c+=1
            temp = []
            for x in range(len(queue)):
                node = queue.pop(0)
                
                if node[0]+1 < len(mat) and mat[node[0]+1][node[1]] == -1:
                    mat[node[0]+1][node[1]] = c
                    temp.append((node[0]+1,node[1]))
                    
                if node[0]-1 >=0 and mat[node[0]-1][node[1]] == -1:
                    mat[node[0]-1][node[1]] = c
                    temp.append((node[0]-1,node[1]))
                    
                if node[1]+1 < len(mat[0]) and mat[node[0]][node[1]+1] == -1:
                    mat[node[0]][node[1]+1] = c
                    temp.append((node[0],node[1]+1))
                    
                if node[1]-1>=0 and mat[node[0]][node[1]-1] == -1:
                    mat[node[0]][node[1]-1] = c
                    temp.append((node[0],node[1]-1))
                    
            queue = temp
            
        return mat
                    
                    
                
                
            
                            
                    
                            
                    
                    
