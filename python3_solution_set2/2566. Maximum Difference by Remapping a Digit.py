class Solution:
    def minMaxDifference(self, num: int) -> int:

        ## max_val -> convert first digit to 9
        ## min_val -> convert first digit to 0

        num = str(num)

        min_num = num.replace(num[0], '0')

        a = '9'
        for x in num:
            if x!='9':
                a = x
                break
        max_num = num.replace(a, '9')

        return int(max_num) - int(min_num)
