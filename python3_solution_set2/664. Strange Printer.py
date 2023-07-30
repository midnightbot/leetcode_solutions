class Solution:
    def strangePrinter(self, s: str) -> int:

        @cache
        def find_ans(s):
            if not s:
                return 0

            cost = find_ans(s[:-1]) + 1
            ch = s[-1]

            for i, c in enumerate(s[:-1]):
                if c == ch:
                    cost = min(cost, find_ans(s[:i+1]) + find_ans(s[i+1:-1]))

            return cost


        return find_ans(s)
