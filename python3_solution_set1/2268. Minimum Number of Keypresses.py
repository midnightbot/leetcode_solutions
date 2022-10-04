##ss
class Solution:
    def minimumKeypresses(self, s: str) -> int:
        
        curr = 1
        adds = 1
        mapping = [0 for x in range(26)]
        press = 0
        
        comp = Counter([x for x in s])
        #print(comp)
        comp = [[x,comp[x]] for x in comp]
        comp = sorted(comp, reverse = True, key = lambda x:x[1])
        
        for x,val in comp:
            if curr == 10:
                adds+=1
                curr = 1
                
            #print(x)
            #print
            mapping[ord(x)-ord('a')] +=adds
            curr+=1
            
        #print(comp)
        #print(mapping)
        for x in s:
            press+= mapping[ord(x) - ord('a')]
            #print(x,mapping[ord(x) - ord('a')])
        return press
        
