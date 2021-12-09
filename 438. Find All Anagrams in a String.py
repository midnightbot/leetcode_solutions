##SS
##not efficient 
##Solution 1
from itertools import combinations
import collections
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(p) > len(s):
            return []
        temp = collections.Counter(p)
        print(temp)
        ans = []
        for x in range(len(s)-len(p)+1):
            temp1 = collections.Counter(s[x:x+len(p)])
            if temp==temp1:
                ans.append(x)
                
        return ans
        
        
