##ss
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        parent = [-1 for x in range(n)]
        
        def find_parent(x):
            if parent[x] == -1:
                return x
            parent[x] = find_parent(parent[x])
            return parent[x]
        
        def union(x,y):
            xs = find_parent(x)
            ys = find_parent(y)
            
            if xs!=ys:
                parent[ys] = xs
                return True
            
            return False
        
        for x in range(len(queries)):
            queries[x].append(x)
            
        queries = sorted(queries, key = lambda x:x[2])
        edgeList = sorted(edgeList, key = lambda x:x[2])
        
        counter = 0
        m = len(edgeList)
        ans = [False for x in range(len(queries))]
        
        ## for every query, we merge all the nodes together that can be connected with edge_costs less than that mentioned in the query
        for x in range(len(queries)):
            while counter < m and edgeList[counter][2] < queries[x][2]:
                union(edgeList[counter][0],edgeList[counter][1])
                counter+=1
                
            ans[queries[x][3]] =  (find_parent(queries[x][0]) == find_parent(queries[x][1]))
            
        return ans
        
        
