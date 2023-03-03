class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:

        ## line parallel to y axis

        ## line is mid of minx and maxx

        minx = min([x[0] for x in points])
        maxx = max([x[0] for x in points])

        line = (minx+maxx)/2

        seen = set()

        for x,y in points:
            seen.add((x,y))

        if line == 0:
            for x,y in points:
                if (-x,y) not in seen:
                    return False

            return True
        else:
            #print(line)
            for x,y in points:
                reflx = -x + (2*line)
                print(reflx)
                if (reflx,y) not in seen:
                    return False

            return True
