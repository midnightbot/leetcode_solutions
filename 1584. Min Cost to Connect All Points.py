##ss
import queue
##kruskals, pick smallest edges if they do not form a cycle
##Solution 1 (Kruskals using priority queue)
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        ##Minimum spanning tree
        ##kruskals algorithms
        if len(points) == 1:
            return 0
        visited = set()
        all_edges = queue.PriorityQueue()
        ans = set()
        for x in range(len(points)-1):
            for y in range(x+1,len(points)):
                
                dist = abs(points[x][0]-points[y][0]) + abs(points[x][1] - points[y][1])
                all_edges.put((dist,points[x],points[y]))
                
                
        cost = 0
        node = all_edges.get()
        cost+=node[0]
        visited.add(tuple(node[1]))
        visited.add(tuple(node[2]))
        while len(visited)!= len(points):
            temp = []
            node = all_edges.get()   
            #print(visited,cost)
            while ((tuple(node[1]) in visited and tuple(node[2]) in visited) or (tuple(node[1]) not in visited and tuple(node[2]) not in visited)):
                if tuple(node[1]) not in visited:
                    temp.append(node)
                node = all_edges.get()
                     
            
            cost+=node[0]
            visited.add(tuple(node[1]))
            visited.add(tuple(node[2]))
            for x in range(len(temp)):
                #if temp[1] not in visited or temp[2] not in visited
                all_edges.put(temp[x])

        return cost
       
        
        
