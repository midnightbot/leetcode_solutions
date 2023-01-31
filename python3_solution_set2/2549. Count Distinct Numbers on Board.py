class Solution:
    def distinctIntegers(self, n: int) -> int:
        seen = {n}

        added = 1

        while added!=0:
            added = 0
            new = set()
            for it in seen:
                for x in range(1,it):
                    if it%x == 1:
                        if x not in seen and x not in new:
                            added+=1
                            new.add(x)

            for it in new:
                seen.add(it)
        #print(seen)
        return len(seen)
