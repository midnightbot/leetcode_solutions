class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []

        # for a position there are 2 options, whether it will be 0 or 1
        # if prev number is 0 for sure it will be 1
        # if prev number is 1 it can be 0 or 1

        def find_ans(curr):
            if len(curr) == n:
                ans.append(curr)
            else:
                if curr[-1] == '0':
                    find_ans(curr+'1')
                else:
                    find_ans(curr+'0')
                    find_ans(curr+'1')

        find_ans('0')
        find_ans('1')
        return ans
        
