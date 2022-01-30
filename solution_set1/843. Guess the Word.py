# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:
##ss
import random
class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        
        
        
        def similarity(word1,word2):
            return sum(i==j for i,j in zip(word1,word2))
        
        
        for x in range(10):
            guessword = random.choice(wordlist)
            sim = master.guess(guessword)
            wordlist = [x for x in wordlist if similarity(x,guessword) == sim]
            
