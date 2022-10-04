##ss
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        dicts = {}
        count  = 0
        for x in range(26):
            dicts[chr(x+ord('a'))] = []
            
        for x in range(len(words)):
            dicts[words[x][0]].append(words[x])
            
        #print(dicts)
        for x in range(len(s)):
            if count == len(words):
                return count
            
            if len(dicts[s[x]])!=0:
                for y in range(len(dicts[s[x]])):
                    thisword = dicts[s[x]].pop(0)
                    if len(thisword) == 1:
                        count+=1
                        
                    else:
                        dicts[thisword[1]].append(thisword[1:])
                        
                        
        return count
        
