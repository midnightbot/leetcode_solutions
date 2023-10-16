class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        curr = []
        i = -1
        ans = []

        for x in range(len(words)):
            if words[x] != "prev":
                curr.append(int(words[x]))
                i = len(curr) - 1
            else:
                if i >= 0:
                    ans.append(curr[i])
                    i-=1
                else:
                    ans.append(-1)
        return ans
        
