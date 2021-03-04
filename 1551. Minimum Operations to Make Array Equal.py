class Solution:
    def minOperations(self, n: int) -> int:
        
        if n%2==0:
            temp = int(n/2)
            return temp*temp #sum of n number of odd numbers
        
        if n%2!=0:
            temp = int((n-1)/2)
            return ((temp*temp)+(temp)) # sum of first n even integers
        
        
# find int(avg of array)
#make all numbers equal to avg of array
# you will have equal number of + and - operations
