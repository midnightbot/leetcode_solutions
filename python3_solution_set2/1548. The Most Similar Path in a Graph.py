class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:

        graph = {}

        for a,b in roads:
            if a in graph:
                graph[a].append(b)
            else:
                graph[a] = [b]

            if b in graph:
                graph[b].append(a)
            else:
                graph[b] = [a]

        dp = [[float('inf') for x in range(n)] for y in range(len(targetPath))]

        for x in range(n):
            if names[x] == targetPath[0]:
                dp[0][x] = 0
            else:
                dp[0][x] = 1

        for x in range(1, len(targetPath)):
            for y in range(n):
                for nei in graph[y]:
                    if names[y] == targetPath[x]:
                        dp[x][y] = min(dp[x][y], dp[x-1][nei])
                    else:
                        dp[x][y] = min(dp[x][y], 1+ dp[x-1][nei])

        ## min of last row will be the end point of the path
        ## backtrack to find the ans

        ans = []
        cost = min(dp[-1])
        curr = dp[-1].index(cost)
        
        for x in range(len(targetPath)-1,0,-1):
            ans.append(curr)
            if targetPath[x] == names[curr]:
                for nei in graph[curr]:
                    if dp[x-1][nei] == cost:
                        curr = nei
            else:
                for nei in graph[curr]:
                    if dp[x-1][nei] == cost - 1:
                        curr = nei
                        cost-=1
        ans.append(curr)
        return ans[::-1]
