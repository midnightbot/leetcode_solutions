##ss
class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        ##kruskals using union find
        ##new virtual node 0 made
        ##connected node 0 to all other nodes with cost equal to well cost at that point
        ##no more use of wells from here
        ##given a set of nodes find min way to connect them, this becomes MST problem
        visited = set()
        ans = 0
        for x in range(n):
            pipes.append([0,x+1,wells[x]])
        
        pipes = sorted(pipes, key = lambda x:x[2]) ## as pipes with min cost will be added first, hence sort acc to pipes cost
        print(pipes)
        self.roots = [x for x in range(n+1)]
        
        for x in pipes:
            if self.union(x[0],x[1]):
                ans+=x[2]
                
        return ans
            

        
    def find(self,v): ##returns which group does an eleemnt belong to
        if self.roots[v]!=v:
            self.roots[v] = self.find(self.roots[v])

        return self.roots[v]


    def union(self,u,v): ## merges two groups
        p1 = self.find(u)
        p2 = self.find(v)

        if p1!=p2:
            self.roots[p2] = self.roots[p1]
            return True

        return False
    
        
        
        
        
