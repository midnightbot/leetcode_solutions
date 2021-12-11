##ss
##Simple DP process
##2 branches
##either word[x] will belong to the optimal solution or not belong to the optimal solutions
##part1 if it belongs to the optimal soluion
## cost + self.fnc(words-words[x],letters-words[x])
##part2 if it does not belong in the optimal solution
## self.fnc(words-words[x],letters-words[x])
import collections
import copy
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        ans = []
        wording = []
        for x in range(len(words)):
            wording.append(self.getmask(words[x]))
        
        self.getscore(wording,self.getmask(letters),score,ans)
        return max(ans)
            
    ##every word will either be in the optimal solution or not be in the optimal solution
    def getscore(self,words,letters,score,ans):
        #print(words,letters)
        for x in range(len(words)):
            if self.check(words[x],letters):
                ## self.getcost(words[x],score) + self.getscore(words-words[x],letters-words[x]) -> word[x] included in optimal answer
                ## self.getscore(words-words[x],letters) -> word[x] not included in optimal ans
                temp1 = words.copy()
                temp1.pop(x)
                new_letters = letters.copy()
                #print(words[x])
                for y in range(len(words[x])):
                    new_letters[y]-=words[x][y]
                #print(new_letters)
                #print(temp1)
                part1 = self.getcost(words[x],score) + self.getscore(temp1,new_letters,score,ans)
                part2 = self.getscore(temp1,letters,score,ans)
                #print(part1,part2,temp1)
                ans.append(max(part1,part2))
                return max(part1,part2)
            else:
                temp1 = words.copy()
                temp1.pop(x)
                ans.append(self.getscore(temp1,letters,score,ans))
                return self.getscore(temp1,letters,score,ans)
            
                
        if len(words) == 0:
            return 0

    def getmask(self,word):
        ans = [0 for x in range(26)]
        
        for x in range(len(word)):
            ans[ord(word[x])-ord('a')]+=1
            
        return ans
    
    
    def getcost(self,word,score):
        ans = 0
        
        for x in range(len(word)):
            ans+=word[x]*score[x]
        #print(word,score,ans)   
        return ans
    
    def check(self,word,letter):
        for x in range(len(word)):
            if word[x] > letter[x]:
                return False
            
        return True
