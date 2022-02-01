##ss
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        
        ans = [-1 for x in range(len(workers))]
        comp = []

        for x in range(len(workers)):
            for y in range(len(bikes)):
                comp.append((self.dist(workers[x],bikes[y]),x,y))
                
        comp = sorted(comp)
        
        
        wvisited = set()
        bvisited = set()

        #print(comp)        
        c = 0
        for x in range(len(comp)):
            if c == len(workers):
                return ans
            
            elif comp[x][1] not in wvisited and comp[x][2] not in bvisited:
                
                    ans[comp[x][1]] = comp[x][2]
                    bvisited.add(comp[x][2])  
                    wvisited.add(comp[x][1])
                    c+=1
                
        return ans
        
        
        
    def dist(self,worker,bike):
        
        return abs(worker[0]-bike[0]) + abs(worker[1]-bike[1])
        
