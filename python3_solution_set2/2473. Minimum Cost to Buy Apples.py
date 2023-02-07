class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:

        ## for each city find minCost

        g = {x:[] for x in range(1,n+1)}

        for x,y,cost in roads:
            g[x].append([y,cost])
            g[y].append([x,cost])

        ## graph is ready

        def find_min_cost(start):
            q = [(0,start)]
            dist = {x:float('inf') for x in range(1,n+1)}

            dist[start] = 0
            ans = float('inf')
            while q:
                cost, top = heapq.heappop(q)

                ans = min(ans, (k+1)*cost + appleCost[top-1])

                for nei, c in g[top]:
                    if dist[nei] > cost + c:
                        dist[nei] = cost + c
                        heapq.heappush(q,(dist[nei],nei))

            return ans

        ans = []
        for x in range(1,n+1):
            ans.append(find_min_cost(x))

        return ans

        
