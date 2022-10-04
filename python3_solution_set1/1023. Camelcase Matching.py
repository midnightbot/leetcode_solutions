##ss
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        
        ans = [False for x in range(len(queries))]
        
        
        for indx,x in enumerate(queries):
            
            i = 0
            n = len(x)
            j = 0
            #print(x)
            def counts(strs):
                c = 0
                
                for x in strs:
                    if ord('A') <= ord(x) <= ord('Z'):
                        c+=1
                        
                return c
            
            while i < n:
                if ord('A') <= ord(x[i]) <= ord('Z') and x[i]!=pattern[j]:
                    break
                    
                elif x[i] == pattern[j]:
                    j+=1
                    
                if j == len(pattern):
                    if counts(x[i+1:]) == 0:
                        break
                    else:
                        j-=1
                        break
                        
                    
                i+=1
                
            if j == len(pattern):
                ans[indx] = True
                
        return ans
        
