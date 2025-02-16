class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:

        for x in range(len(s)-k+1):
            subs = s[x:x+k]
            if len(set(subs)) == 1 and ((x-1>=0 and s[x-1]!=s[x]) or (x-1 < 0)) and ((x+k < len(s) and s[x]!=s[x+k]) or (x+k >= len(s))):
                return True

        return len(s)==1 and k == 1
        
