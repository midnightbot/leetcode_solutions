class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        ##naive solution , make every node as root and try out the combination
        
        ##n * O(m+n)
        ##n^3
        
        ##think of better solutions
        
        ##logic2 keep on removing the leaf nodes
        
        ans = []
        
        if n<=0:
            return ans
        elif n == 1:
            ans = [0]
            return ans
        elif n == 2:
            return [0,1]
        
        degree = [0 for x in range(n)]
        adj = [[] for x in range(n)] 
        
        for x in range(len(edges)):
            degree[edges[x][0]]+=1
            degree[edges[x][1]]+=1
            
            adj[edges[x][0]].append(edges[x][1])
            adj[edges[x][1]].append(edges[x][0])
            
            
        queue = []
        visit = [x for x in range(n)]
        for x in range(n):
            if degree[x] == 1:
                queue.append(x)
                visit.remove(x)
                
        #print(queue)
        print(adj)
        
        
        while len(visit) > 2:
            
            for n in range(len(queue)):
                node = queue.pop(0)
                for m in adj[node]:
                    degree[m]-=1
                    if degree[m] == 1 and m in visit:
                        queue.append(m)
                        visit.remove(m)
                    
        ans = []
        print(degree)
        for x in range(len(degree)):
            if degree[x] > 1:
                ans.append(x)
                
        return ans
            
        
        
        
        
        
