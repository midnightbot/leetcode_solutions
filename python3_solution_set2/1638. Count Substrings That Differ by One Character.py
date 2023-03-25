class Solution:
    def countSubstrings(self, s: str, t: str) -> int:

        counter = {}
        n = len(t)
        m = len(s)
        ans = 0
        ## create all possibilites of a string
        ## abc -> .bc, a.c, ab.
        def create_pattern(strs):
            ans = []
            for x in range(len(strs)):
                ans.append(strs[:x] + '.' + strs[x+1:])
            return ans

        ## store all patterns of string t
        for x in range(n):
            for y in range(x+1,n+1):
                #print(t[x:y])
                curr_s = t[x:y]
                p = create_pattern(curr_s)
                for it in p:
                    counter[it] = counter.get(it,0) + 1

                counter[curr_s] = counter.get(curr_s,0)+1

        ## for each substring s
        ## find all patterns for the substring
        ## find the number of matching patterns in counter
        ## subtract the number of same strings
        for x in range(m):
            for y in range(x+1, m+1):
                curr_s = s[x:y]
                p = create_pattern(curr_s)
                for it in p:
                    if it in counter:
                        ans+=counter[it]
                        if curr_s in counter:
                            ans-=counter[curr_s]
                            
        return ans
