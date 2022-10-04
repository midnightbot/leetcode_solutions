class Solution:
    def countTriples(self, n: int) -> int:
        
        count = 0
        
        for x in range(1,n):
            for y in range(1,n):
                temp = x**2 + y**2
                
                check = temp ** 0.5
                #print(check)
                if check.is_integer() and int(check)<=n:
                    count+=1
                    
                        
                        
                        
        return count
            
        
