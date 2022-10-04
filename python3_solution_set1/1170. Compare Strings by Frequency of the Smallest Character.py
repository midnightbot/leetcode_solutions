##ss
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        comp = []
        anss = []
        for x in range(len(words)):
            ans = self.make_freq(words[x])
            comp.append(ans)
            
        for x in range(len(queries)):
            queries[x] = self.make_freq(queries[x])
        
        comp = sorted(comp)
        for x in range(len(queries)):
            var = False
            for y in range(len(comp)):
                if comp[y] > queries[x]:
                    anss.append(len(comp) - y)
                    var = True
                    break
                    
            if var == False:
                anss.append(0)
                    
        return anss
    def make_freq(self,word):
        dicts = [0 for x in range(26)]
        
        for x in range(len(word)):
            dicts[ord(word[x])-ord('a')]+=1
            
        for x in dicts:
            if x > 0:
                return x
        
