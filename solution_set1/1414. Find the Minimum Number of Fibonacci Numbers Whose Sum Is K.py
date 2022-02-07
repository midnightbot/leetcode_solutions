##ss
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        
        temp = []
        
        
        temp.append(1)
        temp.append(1)
        
        while temp[-1] < k:
            temp.append(temp[-1]+temp[-2])
            
        for x in range(len(temp)-1,-1,-1):
            cnt = 0
            make = k
            for y in range(x,-1,-1):
                if temp[y] <= make:
                    make-=temp[y]
                    cnt+=1
                    
                if make == 0:
                    return cnt
            
            
        
