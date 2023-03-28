class Solution:
    def invalidTransactions(self, t: List[str]) -> List[str]:

        ## name, time, amount, city
        ## invalid if amount > 1000
        ## invalid if within 60 mins with same name in different city

        invalid = set()
        t = [x.split(',') for x in t]
        t = [[x[0], int(x[1]), int(x[2]), x[3]] for x in t]
        t = sorted(t, key = lambda x:x[1])
        

        for x in range(len(t)):
            for y in range(x-1,-1,-1):
                if t[x][0] == t[y][0] and t[x][1]-t[y][1]<=60 and t[x][3]!=t[y][3]:
                    invalid.add(x)
                    invalid.add(y)

            if t[x][2] > 1000:
                invalid.add(x)

        ans = [t[x] for x in list(invalid)]
        ans = [[x[0], str(x[1]), str(x[2]), x[3]] for x in ans]
        ans = [",".join(x) for x in ans]
        return ans
