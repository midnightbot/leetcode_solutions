class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:        
        freq = dict(Counter(deliciousness))

        ans = 0

        for x in freq:
            for k in range(22):
                if 2**k - x <=x and 2**k-x in freq:
                    if 2**k - x == x:
                        ans+= freq[x] * (freq[x]-1)//2
                    else:
                        ans+= freq[x] * freq[2**k - x]

        return ans % (10**9 + 7)
        
