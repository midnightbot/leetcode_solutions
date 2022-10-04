##ss
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        
        ##water cell h = 0
        ##adj cell height diff = 1
        ##mat[i][j] = 1 is water cell
        
        ##simple bfs
        
        q = []
        
        ans = [[-1 for x in range(len(isWater[0]))] for y in range(len(isWater))]
        
        
        for x in range(len(isWater)):
            for y in range(len(isWater[0])):
                if isWater[x][y] == 1:
                    ans[x][y] = 0
                    q.append([x,y,0])
                    
        #print(q)
        #self.print_ans(ans)
        
        while q:
            for x in range(len(q)):
                node = q.pop(0)
                
                if node[0]-1 >=0 and ans[node[0]-1][node[1]] == -1:
                    ans[node[0]-1][node[1]] = node[2] + 1
                    q.append([node[0]-1,node[1],node[2]+1])
                    
                if node[0] + 1 < len(ans) and ans[node[0]+1][node[1]] == -1:
                    ans[node[0]+1][node[1]] = node[2] + 1
                    q.append([node[0]+1,node[1],node[2]+1])
                    
                if node[1] -1>=0 and ans[node[0]][node[1]-1] == -1:
                    ans[node[0]][node[1]-1] = node[2] + 1
                    q.append([node[0],node[1]-1,node[2]+1])
                    
                if node[1] + 1 < len(ans[0]) and ans[node[0]][node[1]+1] == -1:
                    ans[node[0]][node[1]+1] = node[2]+1
                    q.append([node[0],node[1]+1,node[2]+1])
                    
                    
        return ans
            
    def print_ans(self,ans):
        for x in range(len(ans)):
            print(ans[x])
