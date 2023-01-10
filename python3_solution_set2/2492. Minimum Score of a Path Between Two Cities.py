class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        parent = [-1 for x in range(n+1)]
        size = [float('inf') for x in range(n+1)]

        def find_parent(x):
            if parent[x] == -1:
                return x
            parent[x] = find_parent(parent[x])
            return parent[x]

        def union(x,y,dist):
            xs = find_parent(x)
            ys = find_parent(y)

            if xs!=ys:
                parent[min(xs,ys)] = max(xs,ys)
                #print(dist)
                size[max(xs,ys)] = min(size[max(xs,ys)], size[min(xs,ys)], dist)
            else:
                size[max(xs,ys)] = min(size[max(xs,ys)], size[min(xs,ys)], dist)

        for x in roads:
            #print(x)
            union(x[0],x[1],x[2])

        #print(size)

        return size[n]


        
