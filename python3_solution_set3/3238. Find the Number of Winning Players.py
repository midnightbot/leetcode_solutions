class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        ans = 0
        maps = {}

        for (x,y) in pick:
            if x not in maps:
                maps[x] = {}
            maps[x][y] = maps[x].get(y,0)+1

        for x in maps:
            maps[x] = max(list(maps[x].values()))
        
        for x in maps:
            if maps[x] > x:
                ans+=1
        return ans
        
