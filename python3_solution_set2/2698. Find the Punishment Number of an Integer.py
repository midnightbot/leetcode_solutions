class Solution:
    def punishmentNumber(self, n: int) -> int:

        ## simple recursion solution

        @cache
        def is_possible(num, sum):
            '''
            Given a num finds if it is possible to break it into substrings
            such that their sum is 'sum'
            '''
            if int(num) == sum:
                return True

            else:
                ans = False
                num = str(num)
                for x in range(1, len(num)):
                    num1 = num[:x]
                    ans = ans or is_possible(num[x:], sum - int(num1))

                return ans

        def is_punishment(n):
            '''
            Given an integer 'n', finds whether it is a punishment number
            '''
            n_2 = n*n
            return is_possible(n_2, n)
        

        result = 0

        ## loop to find all punishment numbers between 1 to n
        for x in range(1, n+1):
            if is_punishment(x):
                result += x*x

        return result
