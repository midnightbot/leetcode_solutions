class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k >=2 :
            return "".join(sorted(s))

        else:
            all_strs = []

            for x in range(len(s)):
                all_strs.append(s[x:]+s[:x])

            all_strs.sort()
            return all_strs[0]
