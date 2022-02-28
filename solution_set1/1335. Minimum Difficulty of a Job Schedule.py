##ss
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        #prefix = []
        ##simple dp
        ##just try out all combinations
        ##we just have to divide the arr into d arrays minimizing the max work on any day
        ##minimizing the max(max value of any subarray)
        if len(jobDifficulty) < d:
            return -1 
        
        self.ans = float('inf')
        
        @lru_cache(None)
        def split(curr_index,prev_max,d):
            
            
            if d==0 and curr_index < len(jobDifficulty):
                v = max(jobDifficulty[curr_index:])
                return v
                self.ans = min(self.ans, thisans + v)
                
                
            elif d > 0 and curr_index < len(jobDifficulty):
                a = split(curr_index+1, max(prev_max, jobDifficulty[curr_index]), d)
                
                b = max(prev_max, jobDifficulty[curr_index]) + split(curr_index+1, 0, d-1)
                return min(a,b)
            
            else:
                return float('inf')
                
        return split(0,0,d-1)
        #return self.ans
                
