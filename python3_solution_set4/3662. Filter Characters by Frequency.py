class Solution:
    def filterCharacters(self, s: str, k: int) -> str:

        temp = Counter(s)
        ans = ''

        for x in s:
            if temp[x] < k:
                ans+=x

        return ans
        
