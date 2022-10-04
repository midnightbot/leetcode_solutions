##ss
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        start = set()
        
        end = set()
        
        for x in range(len(paths)):
            start.add(paths[x][0])
            end.add(paths[x][1])
            
        ##setA -setB gives elements present in A but not in B
        return list(end - start)[0]
        
