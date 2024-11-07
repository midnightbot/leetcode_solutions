class Solution:
    def largestCombination(self, candidates: List[int]) -> int:

        can = [format(x,'b') for x in candidates]
        maxs = max([len(x) for x in can])

        for x in range(len(can)):
            diff = maxs - len(can[x])
            can[x] = "".join(["0" for i in range(diff)]) + can[x]

        ans = {x:0 for x in range(maxs)}

        for x in range(len(can)):
            for y in range(len(can[x])):
                if can[x][y] == '1':
                    ans[y]+=1

        
        return max(ans.values())

        
