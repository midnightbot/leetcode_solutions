class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        
        ## Simple line sweep algorithm
        ## Time Complexity : O(nlogn)
        ## Space Complexity : O(n)
        
        intervals = sorted(intervals, key = lambda x:x[0])
        dicts = {}
        
        ## where an interval starts overlap+=1
        ## where an interval ends overlap-=1
        ## since [1,5] and [5,8] is an overlap
        ## we add [1,4.99] and [5,7.99] to avoid this miscalculation
        
        ## max overlap at any given point will be the number of groups required
        for x,y in intervals:
            a = x - 0.01
            if a in dicts:
                dicts[a]+=1
                
            else:
                dicts[a] = 1
                
            if y in dicts:
                dicts[y]-=1
            else:
                dicts[y] = -1
                
            
        t = []
        
        for x in dicts:
            t.append([x,dicts[x]])
            
        t = sorted(t, key = lambda x:x[0])
        
        ans = 0
        curr = 0
        for x,y in t:
            curr+=y
            ans = max(ans, curr)
            
        return ans
                
            
            
        
