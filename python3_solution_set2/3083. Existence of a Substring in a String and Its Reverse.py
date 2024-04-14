class Solution:
    def isSubstringPresent(self, s: str) -> bool:

        seen = set()
        for x in range(len(s)):
            for y in range(x+2, len(s)+1):
                seen.add(s[x:y])

        new_s = s[::-1]
        for x in range(len(new_s)):
            for y in range(x+2, len(new_s)+1):
                if new_s[x:y] in seen:
                    return True

        return False
        
