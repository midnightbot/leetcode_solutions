class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = []
        prev = word[0]
        count = 1
        for x in range(1,len(word)):
            if word[x] == prev:
                count+=1
            else:
                res.append(count)
                prev = word[x]
                count = 1
        res.append(count)
        
        return sum(res)-len(res)+1

        
