# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        c = 0
        
        while c < 40:
            a = rand7()
            b = rand7()

            c = b + (a-1)*7
            
        return 1 + (c-1)%10
