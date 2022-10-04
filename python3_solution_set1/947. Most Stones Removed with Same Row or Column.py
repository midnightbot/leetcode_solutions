##ss

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        parent = [-1 for x in range(len(stones))]
        rowdict = {}
        coldict = {}
        count = [len(stones)]
        ##simple union find operation
        ##as soon as a new stone is added, check if its row or its col contains some other stone, if it does contain, combine groups of both the stones
        
        ##from a particular group of n stones n-1 of the stone can be removed
        ##therefore total number of stones that can be removed is len(stones) - total groups
        def find_parent(x):
            if parent[x] == -1:
                return x
            
            parent[x] = find_parent(parent[x])
            
            return parent[x]
        
        def union(x,y):
            xs = find_parent(x)
            ys = find_parent(y)
            
            if xs!=ys:
                count[0]-=1
                parent[xs] = ys
                
                
        for x in range(len(stones)):
            
            if stones[x][0] in rowdict:
                union(stones.index(rowdict[stones[x][0]][0]),x)
                
            if stones[x][1] in coldict:
                union(stones.index(coldict[stones[x][1]][0]),x)
            ##    
            if stones[x][0] in rowdict:
                rowdict[stones[x][0]].append(stones[x])
                
            else:
                rowdict[stones[x][0]] = [stones[x]]
                
            if stones[x][1] in coldict:
                coldict[stones[x][1]].append(stones[x])
                
            else:
                coldict[stones[x][1]] = [stones[x]]
                
        return len(stones) - count[0]
                
        
