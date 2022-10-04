class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        
        A = sorted(A)
        counter = 0
        for x in range(len(A)-1):
            
            if A[x]==A[x+1]:
                counter+=1
            else:
                counter=0
                
            if counter==int(len(A)/2)-1:
                return A[x]
        
        
