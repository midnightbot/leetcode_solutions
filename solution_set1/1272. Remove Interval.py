##ss
class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        
        
        
        ans = []
        
        def intersect(interval,remove):
            ##perfect intersect
            if interval == remove:
                remove = [-float('inf'),-float('inf')]
                return None,None
            
            ##left intersect
            elif remove[0] <= interval[0] and remove[1] > interval[0] and remove[1] <= interval[1]:
                
                a,b = [remove[1],interval[1]],None
                remove = [-float('inf'),-float('inf')]
                return a,b
            
            ##right intersect
            elif remove[0] > interval[0] and remove[0]< interval[1] and remove[1] >= interval[1]:
                
                a,b = [interval[0],remove[0]],None
                remove = [interval[1],remove[1]]
                return a,b
            
            ##full-intersect
            elif remove[0] < interval[0] and remove[1] > interval[1]:
                remove = [interval[1],remove[1]]
                return None,None
            
            ##interval is bigger than full of remove interval
            elif remove[0] > interval[0] and remove[1] < interval[1] and (interval[0] < remove[0] < interval[1]):
                
                cal1,cal2 =  [interval[0],remove[0]] , [remove[1],interval[1]]
                remove = [-float('inf'),-float('inf')]
                return cal1,cal2
            
            ##no intersection between the two arrays
            else:
                return interval,None
            
            
        for x in range(len(intervals)):
            a,b = intersect(intervals[x],toBeRemoved)
            if a is not None:
                ans.append(a)
            if b is not None:
                ans.append(b)
                
        return ans
            
        
