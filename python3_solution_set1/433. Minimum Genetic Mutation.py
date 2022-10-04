##ss
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        diff = []
        
        for x in range(len(start)):
            if start[x]!=end[x]:
                diff.append(x)
                
        def find_diff(comp1,comp2):
            c = 0
            for x in range(len(comp1)):
                if comp1[x]!=comp2[x]:
                    c+=1
                    
            return c
        
        
        g = {x:[] for x in bank}
        g[start] = []
        for x in range(len(bank)):
            for y in range(len(bank)):
                if find_diff(bank[x],bank[y]) == 1:
                    g[bank[x]].append(bank[y])
                    g[bank[y]].append(bank[x])
                    
        for x in range(len(bank)):
            if find_diff(bank[x],start) == 1:
                g[start].append(bank[x])
                
        q = [(start,0)]
        visited = set()
        visited.add(start)
        while q:
            node,cost = q.pop(0)
            
            if node == end:
                return cost
            
            else:
                for nei in g[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei,cost + 1))
                        
        return -1
                
