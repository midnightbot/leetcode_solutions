##ss
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        
        ans = []
        
        for x in range(len(s)):
            t1 = False
            t2 = False
            for m in range(x,len(s)):
                if s[m] == c:
                    t1 = True
                    break
                    
            for n in range(x,-1,-1):
                if s[n] == c:
                    t2 = True
                    break
            
            if t1 == False:
                ans.append(x-n)
                
            elif t2 == False:
                ans.append(m-x)
                
            else:
                ans.append(min(x-n,m-x))
                
        return ans
            #ans.append(min)
        
        
