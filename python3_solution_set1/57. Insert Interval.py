##ss
##Reusing code from Q56. Merge Intervals
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        intervals = sorted(intervals, key = lambda x:x[0])
        
        ans = []
        
       
        temp = [intervals[0][0],intervals[0][1]]
        
        
        #print(intervals)
        for x in range(1,len(intervals)):
            
            if intervals[x][0] <= temp[1]:
                temp[1] = max(temp[1],intervals[x][1])
                
            else:
                ans.append(temp)
                temp = [intervals[x][0],intervals[x][1]]
        ans.append(temp)        
        return ans
        
