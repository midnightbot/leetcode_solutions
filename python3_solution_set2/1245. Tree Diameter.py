class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:

        ## two bfs

        n = len(edges)
        g = {x:[] for x in range(n+1)}

        for x,y in edges:
            g[x].append(y)
            g[y].append(x)

        def do_bfs(curr):
            q = [(curr,0)]
            seen = set()

            while q:
                node,dist = q.pop(0)
                seen.add(node)

                for nei in g[node]:
                    if nei not in seen:
                        q.append([nei, dist+1])

            return node,dist

        farthest1, distance1 = do_bfs(0)
        farthest2, distance2 = do_bfs(farthest1)
        return distance2

                



        
