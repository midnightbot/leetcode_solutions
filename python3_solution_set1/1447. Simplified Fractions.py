##ss
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ##number of fractions
        ans = []
        seen = {}
        
        for deno in range(1,n+1):
            for nume in range(1,deno):
                temp = nume / deno
                
                if temp not in seen:
                    seen[temp] = str(nume) + "/" + str(deno)
                    
        for x in seen:
            ans.append(seen[x])
            
        return ans
            
        
