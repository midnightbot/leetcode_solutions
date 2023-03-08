import bisect
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        
        ## water from 0 to n
        ## find min arrays such that their union covers 0 to n

        dist = [[max(0, x-ranges[x]), min(x+ranges[x],n)] for x in range(len(ranges))]

        dist = sorted(dist, key = lambda x:(x[0], -x[1]))
        #print(dist)
        ans = 0
        curr_pos = 0
        end = 0
        
        for xleft, xright in dist:
            if xleft <= curr_pos:
                end = max(end, xright)
            else:
                ans+=1
                curr_pos = end
                if xleft <= curr_pos:
                    end = max(end, xright)
                #end = max(end, xright)
                
        #print(dist, end, curr_pos)
        if curr_pos!=end:
            ans+=1
        return ans if end == n else -1
