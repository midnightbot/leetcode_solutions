##ss
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        comp = [[] for x in range(len(startTime))]
        
        for x in range(len(startTime)):
            comp[x] = [startTime[x],endTime[x],profit[x]]
            
        comp = sorted(comp, key = lambda x:x[1])
        dp = [0 for x in range(len(startTime))]
        
        #dp[x] be the max profit obtained scheduling jobs 0..x
        ##two options are possible
        ##either job will be in optimal solution or not be in optimal solution
        ##if job not in optimal solution dp[x] = (dp[x-1])
        ##if it is in optimal solution dp[x] = profit(x) + dp[all prev jobs compatible to x]
        
        rel = [0 for x in range(len(startTime))]
        rel[0] = -1
        ##rel[x] gives the positions of the furthest job in range[0..x] compatible with job x
        ##can reduce this time complexity of O(n^2) to O(n.logn) using binary search
        for x in range(1,len(comp)):
            done = False
            for y in range(x-1,-1,-1):
                if comp[x][0] >= comp[y][1]:
                    done = True
                    rel[x] = y
                    break
                    
            if done == False:
                rel[x] = -1
                
        dp[0] = comp[0][2]
        
        for x in range(1,len(dp)):
            if rel[x]!=-1: ##job is compatible with some previous job rel[x]
                dp[x] = max(dp[x-1],comp[x][2] + dp[rel[x]])
                
            else:##this job is not compatible with any previous job
                dp[x] = max(dp[x-1],comp[x][2])
                
            
        return dp[-1]
        
