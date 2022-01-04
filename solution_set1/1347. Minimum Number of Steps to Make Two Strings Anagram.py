##ss
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        s = sorted(s)
        t = sorted(t)
        
        sdicts = {}
        tdicts = {}
        for x in range(26):
            sdicts[chr(x+ord('a'))] = 0
            tdicts[chr(x+ord('a'))] = 0
        for x in range(len(s)):
          
            sdicts[s[x]]+=1
            tdicts[t[x]]+=1

                
        count = 0
        for x in tdicts.keys():
            if tdicts[x] > sdicts[x]:
                count+=tdicts[x] - sdicts[x]
                
        return count
