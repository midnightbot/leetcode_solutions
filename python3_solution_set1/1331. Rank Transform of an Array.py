##ss
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        if len(arr) == 0:
            return arr
        comp = [[x,arr[x],0] for x in range(len(arr))]
        
        comp = sorted(comp, key = lambda x:x[1])
        
        comp[0][2] = 1
        prev = comp[0][1]
        rank = 1
        for x in range(1,len(comp)):
            if comp[x][1] == prev:
                comp[x][2] = comp[x-1][2]
                
            else:
                rank+=1
                comp[x][2] = rank
                prev = comp[x][1]
                
        comp = sorted(comp, key = lambda x:x[0])
        comp = [comp[x][2] for x in range(len(comp))]
        
        return comp
        
