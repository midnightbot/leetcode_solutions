##ss
class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        
        def is_sub(k):
            if k == 0:
                return True
            news = ""
            
            start = 0
            r = removable[0:k]
            r = sorted(r)
            for x in range(k):
                #print(r[x])
                news+= s[start:r[x]]
                start = r[x] + 1
                #print(news,start)
                
            
            news+= s[r[max(k-1,0)]+1:]
            
            #print(news)
            
            i = 0
            j = 0
            
            while i < len(news) and j < len(p):
                if news[i] == p[j]:
                    j+=1
                    
                i+=1
                
                if j == len(p):
                    return True
                
            return j == len(p)
        
        
        l = 0
        r = len(removable)
        
        #print(is_sub(2))
        while l <= r:
            mid = (l+r)//2
            #print(l,r)
            if is_sub(mid):
                l = mid + 1
                
            else:
                r = mid - 1
                
        return r
