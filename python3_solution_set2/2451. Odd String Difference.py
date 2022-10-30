class Solution:
    def oddString(self, words: List[str]) -> str:
        
        def find_ans(strs):
            
            ans = ""
            
            for x in range(1,len(strs)):
                ans+= str(ord(strs[x]) - ord(strs[x-1]))
                ans+=","
                
            return ans
        
        
        wrds = [find_ans(x) for x in words]
        
        temp = Counter(wrds)
        
        
        for x in range(len(wrds)):
            if temp[wrds[x]] == 1:
                return words[x]
        
        
        
