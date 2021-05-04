class Solution:
    def reverse(self, x: int) -> int:
        
        temp = 1
        if x < 0:
            temp = -1
            x = x*-1
        res = [int(y) for y in str(x)]
        res = res[::-1]
        strings = [str(integer) for integer in res]
        a_string = "".join(strings)
        an_integer = int(a_string)
        
        if an_integer < -pow(2,31) or an_integer > (pow(2,31)-1):
            return 0
        else:
            return (an_integer*temp)
        

        
        
