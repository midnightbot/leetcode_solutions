##ss
##Solution 1 (Time Limit Exceeded)
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
    
        queue = [beginWord]
        d = 0
        
        while queue:
            d+=1
            for z in range(len(queue)):
                node = queue.pop(0)
                
                for x in range(len(wordList)):
                    if wordList[x]!=-1 and self.find_diff(node,wordList[x]) == 1:
                        queue.append(wordList[x])
                        if wordList[x] == endWord:
                            return d+1
                        wordList[x] = -1
                        
                        
                for m in range(wordList.count(-1)):
                    wordList.remove(-1)
        return 0
            
    def find_diff(self,word1,word2):
        
        c = 0
        for x in range(len(word1)):
            if word1[x]!=word2[x]:
                c+=1
                
        return c
            
            
            
            
##Solution 2
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        queue = []
        wordList = set(wordList)
        
        queue.append(beginWord)
        
        if endWord not in wordList:
            return 0
        
        d = 0
        while queue:
            d+=1
            for x in range(len(queue)):
                node = queue.pop(0)
                
                for y in range(len(node)): ##finding out all possible words that differ by 1 char from this word
                    for z in range(26):
                        new_word = node[0:y] + chr(z+97) + node[y+1:len(node)]
                        
                        if new_word in wordList:
                            queue.append(new_word)
                            wordList.remove(new_word)
                            
                        if new_word == endWord:
                            return d+1
                        
        return 0
