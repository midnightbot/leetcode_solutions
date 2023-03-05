class Solution:
    def splitNum(self, num: int) -> int:
        num = [str(x) for x in str(num)]
        num.sort()

        a = ''
        b = ''
        for x in range(len(num)):
            if x%2==0:
                a+=num[x]
            else:
                b+=num[x]

        return int(a) + int(b)
