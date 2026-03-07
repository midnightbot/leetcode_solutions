class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        temp = Counter([x for x in str(n)])
        mins = min(temp.values())

        ans = float('inf')

        for x in temp:
            if temp[x] == mins:
                ans = min(ans, int(x))

        return ans
        
