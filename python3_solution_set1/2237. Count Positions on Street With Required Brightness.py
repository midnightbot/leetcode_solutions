##ss
class Solution:
    def meetRequirement(self, n: int, lights: List[List[int]], r: List[int]) -> int:
        
        
        
        comp = [0 for x in range(n+1)]
        
        for l1,l2 in lights:
            comp[max(0,l1-l2)]+=1
            comp[min(n,l1+l2+1)]-=1
            
        pre = []
        s = 0
        for x in comp:
            s+=x
            pre.append(s)
            
        #print(pre)
        return sum(actual >= needed for [actual,needed] in zip(pre,r))
    
              
