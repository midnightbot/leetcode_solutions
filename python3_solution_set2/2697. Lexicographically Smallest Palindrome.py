class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        ans = ['0' for x in range(len(s))]

        for x in range(len(s)//2):
            c1 = s[x]
            c2 = s[-x-1]
            if c1!=c2:
                ans[x] = min(c1,c2)
                ans[-x-1] = min(c1,c2)
            else:
                ans[x] = c1
                ans[-x-1] = c2

        if len(s)%2!=0:
            ans[len(s)//2] = s[len(s)//2]

        return "".join(ans)
