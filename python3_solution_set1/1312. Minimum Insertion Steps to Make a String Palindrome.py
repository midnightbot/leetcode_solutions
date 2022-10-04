##ss
##simple recursion
class Solution:
    def minInsertions(self, s: str) -> int:
        
        
        ##dp[x][y] = ans for string[x:y]
        
            
        @lru_cache(None)    
        def expand(x,y):
            #print(x,y)
            if y == x or x > y: ## if only single word, answer will be zero
                return 0
            
            if y > x:
                if s[y] == s[x]: ## if ending start and end word are same compare x+1 y-1
                    #dp[x][y] = expand()
                    return expand(x+1,y-1)
                
                else: 
                    ##either a new char inseted at begn or at end
                    ##new char ar begn then match x+1,y
                    ##new char at end then match x,y-1
                    return 1 + min(expand(x+1,y),expand(x,y-1))
        
                        
        return (expand(0,len(s)-1))
