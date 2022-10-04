class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        
        
        if A[0]<=A[len(A)-1]:
            a1=sorted(A)
        else:
            a1=sorted(A,reverse=True)
            
        for x in range(len(A)):
            if A[x]!=a1[x]:
                return False
            
        return True
        
