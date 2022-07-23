import bisect
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x:(x[0],x[1]))
        p = []
        comp = [x[0] for x in intervals]
        #print(intervals)
        for x in range(len(intervals)):
            p.append(bisect.bisect_left(comp, intervals[x][1]))
        
        @cache
        def find_ans(indx):
            if indx == len(intervals):
                return 0
            else:
                return max(1 + find_ans(p[indx]), find_ans(indx+1))
            
            
        ans = 0
        for x in range(len(intervals)):
            ans = max(ans, find_ans(x))
            
        return len(intervals) - ans
        
