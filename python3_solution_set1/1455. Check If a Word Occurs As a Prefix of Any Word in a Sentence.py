##ss
class Solution:
    def isPrefixOfWord(self, sentence: str, s: str) -> int:
        
        comp = sentence.split(" ")
        for x in range(len(comp)):
            if len(comp[x]) >= len(s) and comp[x][:len(s)] == s:
                return x+1
            
        return -1
        
