from itertools import permutations
import math
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
        s = [''.join(p) for p in permutations(str(n))]
        #print(s)
        for x in s:
            if x[0]!="0" and bin(int(x)).count('1')==1:
                return True
            
        return False
