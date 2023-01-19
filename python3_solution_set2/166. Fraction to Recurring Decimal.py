class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = ''
        if numerator*denominator < 0:
            sign = '-'
            numerator = abs(numerator)
            denominator = abs(denominator)

        l = numerator // denominator
        r = numerator % denominator
        
        if r == 0:
            return sign + str(l)
        ans = sign + str(l) + '.'

        i = 0
        seen = {r:i}
        result = ''
        while r%denominator:
            r*=10
            i+=1

            rem = r % denominator
            result+=str(r//denominator)

            if rem in seen:
                result = result[:seen[rem]] + '(' + result[seen[rem]:] + ')'
                return ans + result
            seen[rem] = i
            r = rem

        return ans + result


        return ans
        
