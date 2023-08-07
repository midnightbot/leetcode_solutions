class Solution:
    def finalString(self, s: str) -> str:
        ans = ''

        for x in s:
            if x!='i':
                ans+=x
            else:
                ans = ans[::-1]

        return ans
