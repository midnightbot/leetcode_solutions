class Solution:
    def findValidPair(self, s: str) -> str:
        temp = Counter(s)

        for x in range(len(s)-1):
            p1 = s[x]
            p2 = s[x+1]
            if p1!=p2 and temp[p1] == int(p1) and temp[p2] == int(p2):
                return p1+p2

        return '' 
        
