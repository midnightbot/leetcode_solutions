##ss
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        if ch in word:
            indx = word.index(ch)
        
            return word[0:indx+1][::-1] + word[indx+1: len(word)]
        else:
            return word
        
