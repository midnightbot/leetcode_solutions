##ss
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        ##simple dfs or topological sorting
        ##first and last elem only have one adj
        
        adj = {}
        visited = set()
        ans = []
        for x in range(len(adjacentPairs)):
            if adjacentPairs[x][0] in adj:
                adj[adjacentPairs[x][0]].append(adjacentPairs[x][1])
                
            else:
                adj[adjacentPairs[x][0]] =[adjacentPairs[x][1]]
                
                
                
            if adjacentPairs[x][1] in adj:
                adj[adjacentPairs[x][1]].append(adjacentPairs[x][0])
                
            else:
                adj[adjacentPairs[x][1]] =[adjacentPairs[x][0]]
                
        startnode=-1
        for x in adj:
            if len(adj[x]) == 1:
                startnode = x
                break
                
        
        ans.append(startnode)
        visited.add(startnode)
        for x in range(len(adjacentPairs)):
            for z in adj[startnode]:
                if z not in visited:
                    ans.append(z)
                    visited.add(z)
                    startnode = z
                    break
                    
        return ans
                
        
