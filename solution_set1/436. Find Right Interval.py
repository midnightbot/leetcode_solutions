##ss
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        ## startj >= endi
        ## startj is min
        
        intervals = [[x[0],x[1],c] for c,x in enumerate(intervals)]
        
        intervals = sorted(intervals, key = lambda x:x[0])
        ans = [-1 for x in range(len(intervals))]
        
        def do_work(vals):
            l = 0
            r = len(intervals)
            
            while l < r:
                mid = (l+r)//2
                
                if intervals[mid][0] < vals:
                    l = mid + 1
                    
                else:
                    r = mid
                    
            if l >= len(intervals):
                return -1
            return intervals[l][2]
        
        for x in range(len(intervals)):
            ans[intervals[x][2]] = do_work(intervals[x][1])
            
        return ans
            
