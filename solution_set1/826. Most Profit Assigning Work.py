##ss
class Solution:
    def maxProfitAssignment(self, d: List[int], p: List[int], w: List[int]) -> int:

        comp = [[d[x],p[x]] for x in range(len(d))]
        
        comp = sorted(comp)
        #print(comp)
        
        pre_max = [comp[0][1]]
        
        for x in range(1,len(comp)):
            pre_max.append(max(pre_max[-1],comp[x][1]))
        maxs = max(d)
        pre_max.append(0)
        
        #print(pre_max)
        def do_work(vals):
            #print(vals,maxs)
            if vals >= maxs:
                return -2
            l = 0
            r = len(comp) - 1
            ans = -1
            while l < r:
                #print(l,r)
                mid = l + (r-l)//2
                
                if comp[mid][0] > vals:
                    r = mid
                    
                else:
                    ans = mid 
                    l = mid + 1
             
            
            return ans
        
        result = 0
        
        for x in range(len(w)):
            
            result+=pre_max[do_work(w[x])]
            #print(result)
        return result
                
        
