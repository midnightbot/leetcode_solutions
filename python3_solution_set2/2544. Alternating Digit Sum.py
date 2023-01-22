class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s = str(n)
        return sum([int(s[x]) for x in range(len(str(n))) if x%2==0]) - sum([int(s[x]) for x in range(len(str(n))) if x%2!=0])
