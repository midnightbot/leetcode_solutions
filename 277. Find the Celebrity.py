# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        
        counter = 0
        
        for x in range(n):
            counter = 0
            for y in range(n):
                if knows(y,x) == True and knows(x,y)==False and x!=y:
                    counter+=1
                elif x==y:
                    counter+=1
                else:
                    break
                    
                
                    
            if counter == n:
                return x
        
        return -1
                    
                    
                
        
