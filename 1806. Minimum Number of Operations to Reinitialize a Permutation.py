##ss
class Solution:
    def reinitializePermutation(self, n: int) -> int:
        
        og = [x for x in range(n)]
        
        temp = [x for x in range(n)]
        
        var = False
        c = 0
        old_og = [x for x in range(n)]
        while var!=True:
            c+=1
            #print(temp)
            for x in range(len(temp)):
                if x%2==0:
                    temp[x] = old_og[x//2]
                    
                else:
                    temp[x] = old_og[n//2 + (x-1)//2]
                    
            if temp == og:
                var = True
                
            old_og = copy.copy(temp)
                
        return c
                
        
