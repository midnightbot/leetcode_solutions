##ss
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        
        ##select any node color it
        ##select its neighbors, then color them
        ##continue
        
        if len(paths) == 0:
            return [1 for x in range(n)]
        edges = {}
  
        for x in range(len(paths)):
            if paths[x][0] in edges:
                edges[paths[x][0]].append(paths[x][1])
            else:
                edges[paths[x][0]] = [paths[x][1]]
                
            if paths[x][1] in edges:
                edges[paths[x][1]].append(paths[x][0])
            else:
                edges[paths[x][1]] = [paths[x][0]]
                
        ans = [[1,2,3,4] for x in range(n+1)]
        
        visited = set()
        
        p = 1
        
        while p < len(ans):
            
            if type(ans[p]) == int:
                p+=1
            else:
                ans[p] = ans[p][0]
                
                if p in edges:
                    for nei in edges[p]:
                        if type(ans[nei]) == list and ans[p] in ans[nei]:
                            ans[nei].remove(ans[p])
                        
                p+=1
                
        return ans[1:]
        
        
        
