##ss
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        
        ##0 -> 1
        ##01 -> 2
        ##01 10 -> 4
        ##01 10 10 01 -> 8
        ##01 10 10 01 1001 0110 -> 16
        
        ## 1 indexed
        ##if at even pos prevk = k//2
        ## if at odd pos prevk = k+1/2
        
        path = []
        def find_ans(n,k):
            path.append([n,k])
            if n == 1 and k == 1:
                return 0
            
            elif n == 2 and k == 1:
                return 0
            
            elif n == 2 and k == 2:
                return 1
            
            else:
                if k %2 == 0:
                    return find_ans(n-1,k//2)
                
                else:
                    return find_ans(n-1,(k+1)//2)
                
        start = find_ans(n,k)
        path = path[::-1]
        #print(path)
        for x in range(1,len(path)):
            if start == 0:
                if path[x-1][1] * 2 == path[x][1]:
                    start = 1
                    
                else:
                    start = 0
                
                
            else:
                if path[x-1][1] * 2 == path[x][1]:
                    start = 0
                else:
                    start = 1
                    
        return start
            
