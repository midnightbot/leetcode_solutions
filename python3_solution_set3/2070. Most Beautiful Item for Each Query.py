import bisect
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:

        items = sorted(items, key = lambda x:(x[0], x[1]))
        p = [x[0] for x in items]
        b = [x[1] for x in items]
        b_max = []
        for x in range(len(b)):
            if x == 0:
                b_max.append(b[0])
            else:
                b_max.append(max(b_max[-1],  b[x]))
        ans = []
        # print(items,b_max)
        n = len(items)
        for x in queries:
            indx = bisect.bisect_right(p,x)
            if indx == 0:
                ans.append(0)
            elif indx == 1:
                if p[0] <= x:
                    ans.append(b_max[0])
                else:
                    ans.append(b_max[1])
            elif indx < n:
                ans.append(b_max[indx-1])
            else:
                ans.append(b_max[-1])
        return ans
        
