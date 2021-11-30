class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        
        ans  = 0
        for x in range(len(words1)):
            if words1[x] in words2 and words2.count(words1[x]) == 1 and words1.count(words1[x])==1:
                ans+=1
                
        return ans
        
