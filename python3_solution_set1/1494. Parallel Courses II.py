##ss
##simple recursion
from itertools import combinations
import math
class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        
        graph = {x:[] for x in range(1,n+1)}
        indegree = [0 for x in range(n+1)]
        
        if len(relations) == 0:
            return math.ceil(n/k)
        for x in range(len(relations)):
            graph[relations[x][0]].append(relations[x][1])
            indegree[relations[x][1]]+=1
            
        
        @lru_cache(None)
        def min_sems(ins):
            #print(ins)
            seen = ins.split(",")
            seen = [int(x) for x in seen]
            
            #c = 0
            z = []
            for x in range(len(seen)):
                if seen[x] == 0:
                    z.append(x)
                    
                
            if len(z) == 0:
                return 0
            
            elif len(z) <= k:
                for x in range(len(z)):
                    seen[z[x]]-=1
                    for nei in graph[z[x]]:
                        seen[nei]-=1
                        
                seen = [str(x) for x in seen]
                
                return 1 + min_sems(",".join(seen))
            
            else:
                combs = list(combinations(z,k))
                ans = float('inf')
                for nei in combs:
                    newseen = copy.deepcopy(seen)
                    for elem in nei:
                        newseen[elem] = -1
                        
                        for a in graph[elem]:
                            newseen[a]-=1
                        
                    newseen = [str(x) for x in newseen]
                    
                    ans = min(ans, 1 + min_sems(",".join(newseen)))
                    
                return ans
                    
            
            
            
            
            
        indegree[0] = '-1'   
        for x in range(1,len(indegree)):
            indegree[x] = str(indegree[x])
            
        return min_sems(",".join(indegree))
        #return 0
