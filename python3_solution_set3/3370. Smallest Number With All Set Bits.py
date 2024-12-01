class Solution:
    def smallestNumber(self, n: int) -> int:
        n = format(n, 'b')
        if len(n) == n.count('1'):
            return int(n, 2)
        else:
            return int(''.join(['1' for x in range(len(n))]),2)
        
