##ss
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        ## divide into k palindromes
        
        ## return min replacements required
        
        @cache
        def repl(strs):
            if strs == strs[::-1]:
                return 0
            else:
                if len(strs)%2==0:
                    n = len(strs)//2
                    count = 0
                    for x in range(n):
                        if strs[x]!=strs[-1-x]:
                            count+=1
                            
                    return count
                
                else:
                    n = len(strs)//2
                    count = 0
                    for x in range(n):
                        if strs[x]!=strs[-1-x]:
                            count+=1
                            
                    return count
                
          
        
        @cache
        def find_ans(prev,i,k):
            
            #print(prev,i,k)
            if k == 1 and i < len(s):
                return repl(s[i:])
            
            if i >= len(s):
                return float('inf')
            
            elif k > 1:
                return min(find_ans(prev,i+1,k), repl(s[prev:i+1]) + find_ans(i+1,i+1,k-1))
                
                
        return find_ans(0,0,k)
        
        
