class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:

        ans = []
        n = len(word)
        m = len(sequence)
        x = 0
        #print(len(sequence))
        while x <= m-n+1:
            if sequence[x:x+n] == word:
                ans.append(x)
            x+=1
        
        result = 0
        c = 1
        base = {}
        
        for it in ans:
            base[it] = base.get(it-n,0) + 1
        
        if base.values():
            return max(base.values())
        return 0
                
        
