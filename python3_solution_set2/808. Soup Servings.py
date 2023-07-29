class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1
        @cache
        def find_ans(a,b):
            if a<=0 and b<=0:
                return 0.5

            if a<=0:
                return 1

            if b<=0:
                return 0

            return 0.25*(find_ans(a-4,b) + find_ans(a-3,b-1) + find_ans(a-2,b-2) + find_ans(a-1,b-3))


        n = math.ceil(n/25)
        return find_ans(n,n)
