##ss
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        
        temp = set([word[i: j] for i in range(len(word)) for j in range(i + 1, len(word) + 1)])
        tempp = list(temp)
        ans = 0
        
        for x in range(len(tempp)):
            if tempp[x] in patterns:
                ans+= patterns.count(tempp[x])
                
                
        return ans
        
