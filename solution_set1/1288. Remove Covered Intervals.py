##ss
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals = sorted(intervals, reverse = True, key = lambda x:(x[1]-x[0]))
        
        count  = 0
        
        #intervals = intervals[::-1]
        #print(intervals)
        for x in range(len(intervals)-1):
            if intervals[x]!=-1:
                for y in range(x+1,len(intervals)):
                    if intervals[y]!=-1 and self.iscovered(intervals[x],intervals[y]):
                        count+=1
                        intervals[y] = -1
                    
        return len(intervals) - count
                
                
                
    def iscovered(self,p1,p2):
        #print(p1,p2)
        return p1[0]<=p2[0] and p1[1] >=p2[1]
            
        
