class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:

        return sum([int(i) for i in str(x)]) if x%sum([int(i) for i in str(x)])==0 else -1
        
