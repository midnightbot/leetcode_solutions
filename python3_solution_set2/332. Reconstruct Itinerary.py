class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        graph = {}
        for x,y in tickets:
            if x in graph:
                graph[x].append(y)
            else:
                graph[x] = [y]

        for x in graph:
            graph[x] = sorted(graph[x], reverse = True)

        self.ans = []

        def find_ans(curr):
            if curr in graph:
                while graph[curr]:
                    nei = graph[curr].pop()
                    find_ans(nei)
            self.ans.append(curr)

        find_ans('JFK')
        return self.ans[::-1]

