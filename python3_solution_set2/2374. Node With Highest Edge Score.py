class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        
        n = len(edges)
        
        indegree = {x:0 for x in range(n)}
        
        for it,val in enumerate(edges):
            indegree[val]+=it
            
        temp = []
        
        for x in indegree:
            temp.append([indegree[x],x])
        
        temp = sorted(temp, key = lambda x:[-x[0],x[1]])
        return temp[0][1]
        
