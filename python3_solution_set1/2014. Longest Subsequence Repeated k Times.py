##ss
from itertools import combinations
class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        
        ##just try out all possible combinations
        ## sort by length, sort lexically, start trying all the options that can be made
        fmap = Counter(s)
        
        use = {}
        comp  = []
        for x in fmap:
            if fmap[x] >= k:
                use[x] = fmap[x]
                for z in range(fmap[x]//k):
                    comp.append(x)
                    
        all_opt = []
        
        def check(chck):
            count = 0
            i = 0
            if len(chck) == 0:
                return False
            
            for x in range(len(s)):
                if i == len(chck):
                    return True
                
                elif s[x] == chck[i]:
                    i+=1

                elif len(s) - x < len(chck) - i:
                    return False
                
            return i == len(chck)
            
        
                
        #make_str(0,comp,"")    
        #print(len(s))
        for x in range(1,len(comp)+1):
            all_opt += ["".join(a) for a in list(itertools.permutations(comp, x))]
            
        #print(all_opt)
        all_opt = list(set(all_opt))
        all_opt = sorted(all_opt, reverse = True)
        all_opt = sorted(all_opt, reverse = True, key = lambda x:(len(x)))
        
        #print(all_opt)
        for x in range(len(all_opt)):
            if len(all_opt[x]) * k <= len(s) and check(all_opt[x]*k):
                return all_opt[x]
        
        return ""
