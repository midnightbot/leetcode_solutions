class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        ans = []
        
        for x in range(1,n+1):
            if x%3==0 and x%5==0:
                ans.append("FizzBuzz")
                
            elif x%3==0:
                ans.append("Fizz")
                
            elif x%5==0:
                ans.append("Buzz")
                
            else:
                ans.append(str(x))
                
        return ans
        
