class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        
        def do_words(strs,i):
            if len(strs) - i <= 3:
                return strs
            else:
                return strs[:i+1] + str(len(strs)-i-2) + strs[-1]
            
            
        n = len(words)
        
        ans = [do_words(x,0) for x in words]
        prefix = [0 for x in range(n)]
        
        for x in range(n):
            while True:
                duplicate = set()
                for y in range(x+1,n):
                    if ans[x] == ans[y]:
                        duplicate.add(y)
                    
                if not duplicate:
                    break
                duplicate.add(x)
                for c in duplicate:
                    prefix[c]+=1
                    ans[c] = do_words(words[c], prefix[c])
            
            
            
            
        return ans
