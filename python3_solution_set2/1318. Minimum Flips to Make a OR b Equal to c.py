class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:

        ## make a difference array and look at the positions that are different

        ## if c[i] wants to be 0 but is not flips = a[i] + b[i]

        ## if c[i] want to be 1 but is not flips = 1

        a = format(a,'b')
        b = format(b,'b')
        c = format(c,'b')

        maxs = max(len(a), len(b), len(c))

        if len(a)!=maxs:
            diff = maxs - len(a)
            a = ''.join(['0' for x in range(diff)]) + a
        
        if len(b)!=maxs:
            diff = maxs - len(b)
            b = ''.join(['0' for x in range(diff)]) + b

        if len(c)!=maxs:
            diff = maxs - len(c)
            c = ''.join(['0' for x in range(diff)]) + c
        flips = 0
        for x in range(maxs):
            if c[x] == '0':
                flips+=int(a[x]) + int(b[x])

            elif c[x] == '1':
                if a[x] == '0' and b[x] == '0':
                    flips+=1

        return flips
