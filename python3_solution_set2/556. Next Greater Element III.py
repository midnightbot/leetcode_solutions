class Solution:
    def nextGreaterElement(self, n: int) -> int:

        s = [int(x) for x in str(n)]
        i = len(s) - 1

        while i-1>=0 and s[i] <= s[i-1]:
            i-=1

        if i == 0:
            return -1

        j = i
        while j+1 < len(s) and s[j+1] > s[i-1]:
            j+=1

        s[i-1], s[j] = s[j], s[i-1]
        s[i:] = s[i:][::-1]
        s = [str(x) for x in s]


        
        return int("".join(s)) if 1<=int("".join(s))<=2**31 - 1 else -1
