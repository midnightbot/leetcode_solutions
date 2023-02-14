import math
class Solution:
    def numberOfNodes(self, n: int, queries: List[int]) -> int:

        ans = [0 for x in range(n+1)]

        que = {}
        ## if a query is implemented even number of times
        ## it will bring the tree back to same values 
        ## hence only execute queries that are being executed odd number of times once
        for x in queries:
            if x in que:
                que[x]+=1
            else:
                que[x] = 1

        for x in que:
            que[x]%=2

        queries = []
        for x in que:
            if que[x] == 1:
                queries.append(x)

        @cache
        def find_nei(x):
            q = [x]
            ans = []
            while q:
                top = q.pop(0)
                ans.append(top)
                if 2*top+1 <=n:
                    q.append(2*top+1)
                if 2*top<=n:
                    q.append(2*top)
            return ans

        for x in queries:
            nei = find_nei(x)## update the subtree

            for it in nei:
                ans[it]+=1

        ans = [x%2 for x in ans]

        return ans.count(1)
