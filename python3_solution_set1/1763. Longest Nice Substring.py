##ss
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        opts = [[s[i:j+1],i] for i in range(len(s)-1) for j in range(i+1,len(s))]
        
        opts = sorted(opts, key = lambda x:(-len(x[0]), x[1]))
        
        def check_this(strs):
            small = Counter([x for x in strs if x.islower()])
            bigs = Counter([x.lower() for x in strs if x.isupper()])
            
            return small.keys() == bigs.keys()
        
        #print(opts)
        for x in opts:
            if check_this(x[0]):
                return x[0]
        return ""
