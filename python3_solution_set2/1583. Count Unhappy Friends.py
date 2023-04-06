class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:


        ## (x,y) and (u,v) is invalid
        ## if x prefers u over y
        ## and u prefers x over v
        result = set()
        g = {}

        for indx, f in enumerate(preferences):
            for i,it in enumerate(f):
                g[str(indx) + ',' + str(it)] = i

        def is_conflict(x,y,u,v):
            rank_xu = g[str(x) + ',' + str(u)]
            rank_ux = g[str(u) + ',' + str(x)]
            rank_xv = g[str(x) + ',' + str(v)]
            rank_vx = g[str(v) + ',' + str(x)]
            rank_xy = g[str(x) + ',' + str(y)]

            rank_yu = g[str(y) + ',' + str(u)]
            rank_uy = g[str(u) + ',' + str(y)]
            rank_yv = g[str(y) + ',' + str(v)]
            rank_vy = g[str(v) + ',' + str(y)]
            rank_yx = g[str(y) + ',' + str(x)]

            rank_uv = g[str(u) + ',' + str(v)]
            rank_vu = g[str(v) + ',' + str(u)]

            ans = set()
            ## x unhappy
            if rank_xu < rank_xy and rank_ux < rank_uv:
                ans.add(x)
            if rank_xv < rank_xy and rank_vx < rank_vu:
                ans.add(x)
            ## y unhappy
            if rank_yu < rank_yx and rank_uy < rank_uv:
                ans.add(y)
            if rank_yv < rank_yx and rank_vy < rank_vu:
                ans.add(y)

            return ans

        for x in range(len(pairs)):
            for y in range(len(pairs)):
                if x!=y:
                    temp = is_conflict(pairs[x][0], pairs[x][1], pairs[y][0], pairs[y][1])
                    result = result.union(temp)
        return len(result)
