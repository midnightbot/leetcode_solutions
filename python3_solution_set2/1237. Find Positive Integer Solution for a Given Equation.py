"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:

        ## z = a*x (operation) b*y

        ## try to find this operation and a,b
        ## then generate ans pairs
        '''
        ans = []
        ## rather than trying all y for all x
        ## keep a pointer for y
        for x in range(1,1001):
            for y in range(1,1001):
                if customfunction.f(x,y) == z:
                    ans.append([x,y])


        return ans
        '''
        ## function is monotonically increasin
        ## if f(x,y) == z then f(x+1,k) will be equal to z if k < y

        ans = []
        y = 1001

        for x in range(1,1001):

            while y>1 and customfunction.f(x,y) > z:
                y-=1

            if customfunction.f(x,y) == z:
                ans.append([x,y])

        return ans
             
