# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        ## simple binary search
        left = 0
        right = n
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if guess(mid) == 0:
                return mid
            
            elif guess(mid) == -1:
                right = mid - 1
                
            else:
                left = mid + 1
        
