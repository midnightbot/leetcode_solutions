class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        
        count = 0
        seen = set()
        res = set(restricted)
        graph = {}
        for x,y in edges:
            if x in graph:
                graph[x].append(y)
            else:
                graph[x] = [y]
                
            if y in graph:
                graph[y].append(x)
            else:
                graph[y] = [x]
                
        q = [0]
        seen.add(0)
        while q:
            top = q.pop(0)
            if top not in res:
                count+=1
            for nei in graph[top]:
                if nei not in seen and nei not in res:
                    q.append(nei)
                    seen.add(nei)
        
        return count
        
