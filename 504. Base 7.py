class Solution:
    def convertToBase7(self, num: int) -> str:
        temp = num
        num = abs(num)
        result = num % 7
        power = 1
        while num//7 != 0:
            num = num//7
            result += ((num % 7) * 10**power)
            power += 1
        return str(result) if temp >= 0 else '-' + str(result)
