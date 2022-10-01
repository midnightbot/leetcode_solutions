class Solution:
    def equalFrequency(self, word: str) -> bool:
        
        def is_ans(strs):
            t = Counter(strs)
            t2 = Counter(t.values())
            return len(Counter(t2).keys()) == 1
        
        
        for x in range(len(word)-1):
            new_s = word[:x] + word[x+1:]
            #print(new_s)
            if is_ans(new_s):
                return True
            
        return False
