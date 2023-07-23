class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:

        ans = []

        for x in words:
            temp = x.split(separator)
            for it in temp:
                if it!='':
                    ans.append(it)
        return ans
