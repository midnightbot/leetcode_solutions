class Solution:
    def sortPeople(self,  n: List[str], h: List[int]) -> List[str]:
        
        arr = [[h[x],n[x]] for x in range(len(n))]
        arr = sorted(arr, key = lambda x:(-x[0],x[1]))
        
        return [x[1] for x in arr]
