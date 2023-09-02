class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        a = [s1[x] for x in range(0,len(s1),2)]
        b = [s1[x] for x in range(1,len(s1),2)]

        c = [s2[x] for x in range(0,len(s2),2)]
        d = [s2[x] for x in range(1,len(s2),2)]

        return sorted(a) == sorted(c) and sorted(b) == sorted(d)
        
