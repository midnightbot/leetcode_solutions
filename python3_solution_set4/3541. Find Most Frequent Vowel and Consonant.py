class Solution:
    def maxFreqSum(self, s: str) -> int:
        s = Counter(s)
        val1 = [0]
        val2 = [0]

        for i in s:
            if i in 'aeiou':
                val1.append(s[i])
            else:
                val2.append(s[i])

        val1.sort()
        val2.sort()

        return val1[-1] + val2[-1]        
