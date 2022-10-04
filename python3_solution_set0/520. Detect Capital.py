class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        caps = 0
        
        for x in range(len(word)):
            if ord(word[x])>=65 and ord(word[x])<=90:
                caps+=1
                
        if caps == 0:
            return True
        
        elif caps==1:
            if caps==1 and ord(word[0])>=65 and ord(word[0])<=90:
                return True
            else:
                return False
            
        elif caps == len(word):
            return True
        
