import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sum_even = sum([x if x%2==0 else 0 for x in range(1,(2*n)+1)])
        sum_odd = sum([x if x%2!=0 else 0 for x in range(1,(2*n)+1)])
        return math.gcd(sum_even, sum_odd)
        
