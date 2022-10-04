##ss
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        ##simple recursion
        
        self.result = []
        self.expand(s,0,"",wordDict,"")
        return self.result
        
    def expand(self,s,pointer,curr,wordDict,thisans):
        #print(thisans)
        if pointer == len(s) and curr in wordDict: ##last formed word also in dict so this is valid answer
            thisans+=" "+  curr
            self.result.append(thisans[1:])
            
            
        elif pointer < len(s):
            if curr + s[pointer] in wordDict: ##if this curr word is present in dict try splitting out the rest string into valid words
                self.expand(s,pointer+1,"",wordDict,thisans+" "+curr+s[pointer])
                
            ##curr = curr + s[pointer]
            self.expand(s,pointer+1,curr+s[pointer],wordDict,thisans)
                
            
        
