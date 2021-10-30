class Solution:
    def numSquares(self, n: int) -> int:
        
        
        squares = [i*i for i in range(0,int(math.sqrt(n))+1)]
        opt = [float('inf')]*(n+1)
        
        opt[0] = 0
        
        for x in range(1,n+1):
            for sqr in squares:
                if x < sqr:
                    break
                    
                else:
                    opt[x] = min(opt[x],opt[x-sqr] + 1)
                    
                    
        return opt[-1]
        
