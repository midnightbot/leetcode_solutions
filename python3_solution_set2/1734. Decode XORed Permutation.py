class Solution:
    def decode(self, encoded: List[int]) -> List[int]:

        n = len(encoded) + 1

        full = 0

        for x in range(1,n+1):
            full^=x

        first = full
        for x in range(1, n-1, 2):
            first^= encoded[x]

        perm = [first]
        for x in range(0,len(encoded)):
            perm.append(perm[-1] ^ encoded[x])
        return perm
