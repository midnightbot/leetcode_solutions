class Solution:
    def maximumValue(self, strs: List[str]) -> int:

        ans = []

        for x in strs:
            try:
                ans.append(int(x))
            except:
                ans.append(len(x))
        return max(ans)
