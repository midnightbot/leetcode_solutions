##SS
## Use set to avoid adding same nodes into the explore queue 
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        counter = 0
        
        queue = set()
        
        for x in range(len(isConnected)):
            for y in range(len(isConnected[0])):
                if isConnected[x][y] == 1:
                    queue.add(tuple((x,y)))
                    counter+=1
                    while queue:
                        
                        node = queue.pop()
                        isConnected[node[0]][node[1]] = -1
                        for z in range(len(isConnected[0])):
                            if isConnected[node[1]][z] == 1:
                                queue.add(tuple((node[1],z)))
                            
        return counter
