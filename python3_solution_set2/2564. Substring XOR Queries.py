class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:

        ## val XOR first = second
        ## val = second XOR first

        queries = [x[0]^x[1] for x in queries]
        
        dicts ={}
        n = len(s)
        
        dicts[int(s[0])] = [0,0]
        for x in range(n):
            if s[x]!='0':
                for y in range(x, min(x+32, n+1)):
                    if x!=y:
                        ints = int(s[x:y],2)
                        if ints not in dicts:
                            dicts[ints] = [x,y-1]
            else:
                if 0 not in dicts:
                    dicts[0] = [x,x]
        ans = []
        if int(s[-1]) not in dicts:
            dicts[int(s[-1])] = [n-1,n-1]
        for q in queries:
            if q in dicts:
                ans.append(dicts[q])
            else:
                ans.append([-1,-1])
        return ans
