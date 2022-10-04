##ss
class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        #dp = [[False for x in range(n)] for y in range(n)]
        
        @cache
        def is_palin(i,j):
            if i > j:
                return True
            
            elif i == j:
                return True
            
            else:
                if s[i] == s[j]:
                    return is_palin(i+1,j-1)
                else:
                    return False
                
            
        @cache        
        def find_ans(prev,i,k):
            if k == 1:
                return is_palin(i,len(s)-1)
            
            elif i > len(s):
                return False
            
            else:
                for it in range(i,len(s)-1):
                    if is_palin(prev,it) and find_ans(it+1,it+1,k-1):
                        return True
                    
                return False
            
            
        t = is_palin(0,n-1) ## precomputing for all sub-strings if they are palindrome
        return find_ans(0,0,3)
