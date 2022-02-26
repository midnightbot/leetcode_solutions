##ss
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        chrs = {}
        rev = {}
        for x in range(len(order)):
            chrs[order[x]] = x
            rev[x] = order[x]
            
        comp = []
        for x in range(len(words)):
            temp = []
            for y in range(len(words[x])):
                temp.append(chrs[words[x][y]])
                
            #temp.append(words[x])
            comp.append(temp)
            
        comp = sorted(comp)
        #print(comp)
        for x in range(len(comp)):
            thisword = ""
            for y in range(len(comp[x])):
                thisword+=rev[comp[x][y]]
                
            if thisword!=words[x]:
                return False
            
        return True
