class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        lens = len(s)
        count = s.count('1')
        return ''.join(['1' for x in range(count-1)] + ['0' for x in range(lens-count)] + ['1'])
        
