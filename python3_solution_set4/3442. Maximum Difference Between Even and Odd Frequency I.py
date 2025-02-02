class Solution:
    def maxDifference(self, s: str) -> int:
        temp = list(Counter(s).values())
        o = []
        e = []

        for x in temp:
            if x%2==0:
                e.append(x)
            else:
                o.append(x)
        e.sort()
        o.sort()

        if o and e:
            return o[-1] - e[0]

        # print(e,o)       
