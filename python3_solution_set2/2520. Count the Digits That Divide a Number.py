class Solution:
    def countDigits(self, num: int) -> int:

        ans = 0

        for x in str(num):
            if x!='0' and num%int(x)==0:
                ans+=1

        return ans
