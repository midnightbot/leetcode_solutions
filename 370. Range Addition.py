class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        
        
        ans  = [0 for x in range(length)]
        
        visited = {}
        for x in range(len(updates)):
            if (str(str(updates[x][0]) +","+str(updates[x][1]))) in visited.keys():
                visited[str(str(updates[x][0]) +","+str(updates[x][1]))]+=updates[x][2]
                
            else:
                visited[str(str(updates[x][0]) +","+str(updates[x][1]))]=updates[x][2]
                
        for x in visited.keys():
            temp = x
            indices = temp.split(",")
            #print(indices)
            val = visited[x]
            c1 = int(indices[0])
            c2 = int(indices[1])
            
            for y in range(c1,c2+1):
                ans[y]+=val
                
                
        return ans
            
        
