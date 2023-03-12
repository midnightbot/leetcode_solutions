class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:

        ans = 0

        for x in range(left, right + 1):
            strs = words[x]
            if strs[0] in 'aeiou' and strs[-1] in 'aeiou':
                ans+=1

        return ans
