##ss
##find cycle -> find distane
class Solution:
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        
        ans = [float('inf') for x in range(n)]
        self.V = n
        tracker = [-1 for x in range(n)]
        ##part1 find the cycle
        ##part2 find min dist of nodes to nodes in the cycle
        
        ##part1 : finding the cycle
        graph = {}
        
        for x in range(len(edges)):
            if edges[x][0] in graph:
                graph[edges[x][0]].append(edges[x][1])
            else:
                graph[edges[x][0]] = [edges[x][1]]
                
            if edges[x][1] in graph:
                graph[edges[x][1]].append(edges[x][0])
            else:
                graph[edges[x][1]] = [edges[x][0]]
         
        visited = set()
        cycle_nodes = []
        def find_cycle(node,parent):
            if node in visited:
                return True, node
            
            for nei in graph[node]:
                if nei == parent:
                    continue
                visited.add(node)
                cycle_nodes.append(node)
                
                a,b = find_cycle(nei, node)
                
                if a == True:
                    return a,b
                
                cycle_nodes.pop()
                visited.remove(node)
                
            return False, None
            
        a,b = find_cycle(0,None)
        #print(cycle_nodes)
        cycle_nodes = cycle_nodes[cycle_nodes.index(b):]
        #print(check_set)
        #print(parent,x,cycle_nodes)
        
        ##part2 finding minimum distance to the cycle
        for x in cycle_nodes:
            ans[x] = 0
            
        visited = set()
        
        q = [] ##[cost,dist]
        
        for x in cycle_nodes:
            q.append([0,x])
            
        #print(graph)
        while q:
            #print(q)
            top = q.pop(0)
            thiscost = top[0]
            thisnode = top[1]

            if thisnode not in visited:
                visited.add(thisnode)
                ans[thisnode] = thiscost
                
                for nei in graph[thisnode]:
                    if nei not in visited:
                        q.append([thiscost+1,nei])
                        
                        #visited.add(nei)
                        
        return ans
        
