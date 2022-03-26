##ss 
##Solution 1 (Brute Force - TLE)
class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        maxpt = -1
        for x in range(len(paint)):
            maxpt = max(maxpt,paint[x][1])
            
        comp = [1 for x in range(maxpt+1)]
        print(comp)
        ans = []
        for x in range(len(paint)):
            load = 0
            for y in range(paint[x][0],paint[x][1]):
                #print(x,y)
                if comp[y] == 1:
                    comp[y] = 0
                    load+=1
                    
            ans.append(load)
            
        return ans
        
 ##Solution 2(Segment Tree TLE)
 class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        ##kind of segment tree
        
        lens = 0
        for x in paint:
            lens = max(lens,x[1])
            
       
        #print(lens)
        slen = 0
        for x in range(100):
            if 2**x >= lens:
                
                slen = 2*(2**x) - 1
                break
              
        
        segtree = [0 for x in range(slen)]
        
        def query(qlow,qhigh,low,high,pos):
            
            if qlow <= low and qhigh >=high: ##total overlap
                #print(low,high)
                if low!=high and high!=qhigh:
                    vals = segtree[low:high+1].count(0)
                    for z in range(low,high+1):
                        segtree[z] = 1
                    return vals
                
                elif low!=high and high == qhigh:
                    vals = segtree[low:high].count(0)
                    for z in range(low,high):
                        segtree[z] = 1
                    return vals

                elif low == high and high!=qhigh:
                    ans = 1 if segtree[low] == 0 else 0
                    segtree[low] = 1
                    return ans
                
                elif low == high and high == qhigh:
                    ans = 1 if segtree[low-1] == 0 else 0
                    segtree[low-1] = 1
                    return ans
                
                return 0
            
            if qlow > high or qhigh < low:
                return 0
            
            
            mid = (low + high)//2
            
            return query(qlow,qhigh,low,mid,2*pos+1) + query(qlow,qhigh,mid+1,high,2*pos+2)
        
        
        ans = []
        
        for x1,x2 in paint:
            ans.append(query(x1,x2,0,slen,0))
            #print(segtree)
        return ans
##Solution 3(Accepted)
class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        
        ans = [0 for x in range(50000)]
        result = []
        
        for x1,x2 in paint:
            c= 0
            while x1 < x2:
                if ans[x1]!=0: ## jump to max index that has been covered considering this tile is covered
                    x1 = ans[x1]
                    
                else:
                    c+=1
                    ans[x1] = x2
                    x1+=1
                    
            result.append(c)
                    
                    
        return result
