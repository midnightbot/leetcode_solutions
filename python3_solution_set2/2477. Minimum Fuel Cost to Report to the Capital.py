class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:

        ## simple dfs Solution
        n = len(roads) + 1

        graph = {x:[] for x in range(0,n)}

        for a,b in roads:
            graph[a].append(b)
            graph[b].append(a)

        def find_ans(city, prev):
            count = 1

            for nei in graph[city]:
                if nei == prev:
                    continue
                count+=find_ans(nei, city)

            if city!=0:
                self.ans += math.ceil(count/seats)
            return count

        self.ans = 0
        find_ans(0,-1)
        return self.ans

