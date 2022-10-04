###ss

##Solution1 (Competition Attempt 76/78 test cases passed)
import heapq
class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        
        ## return subgraph such that it is possible to reach dest from both src1 and src2
        
        
        ## either src1 - dest will be min
        ## or src2 - dest will be min
        ## ans = min(both-min, src1min + src2-src1, src2min + src1 - src2)
        
        parent1 = {x:-1 for x in range(n-1)}
        parent2 = {x:-1 for x in range(n-1)}
        graph = {}
        costs = {}
        ans1 = [float('inf') for x in range(n)]
        ans2 = [float('inf') for x in range(n)]
        
        
        
        for x in range(len(edges)):
            if edges[x][0] in graph:
                graph[edges[x][0]].append([edges[x][1],edges[x][2]])
                
            else:
                graph[edges[x][0]] = [[edges[x][1], edges[x][2]]]
                
            
            if str(edges[x][0]) + "," + str(edges[x][1]) in costs:
                costs[str(edges[x][0]) + "," + str(edges[x][1])] =  min(costs[str(edges[x][0]) + "," + str(edges[x][1])], edges[x][2])
            else:
                costs[str(edges[x][0]) + "," + str(edges[x][1])] = edges[x][2] 
            
        q1 = []
        heapq.heappush(q1,[0,src1])
        ans1[src1] = 0
        visited1 = set()
        while q1:
            node = heapq.heappop(q1)
            
            dist = node[0]
            pt = node[1]
            
            if pt not in visited1:
                visited1.add(pt)
                
                if pt in graph:
                    for nei in graph[pt]:
                        if nei[0] in visited1:
                            continue
                            
                        if dist + nei[1] < ans1[nei[0]]:
                            ans1[nei[0]] = dist + nei[1]
                            
                            parent1[nei[0]] = pt
                            heapq.heappush(q1,[ans1[nei[0]], nei[0]])
            
        #print(ans1)
        
        q1 = []
        heapq.heappush(q1,[0,src2])
        ans2[src2] = 0
        visited2 = set()
        #print(q1)
        while q1:
            node = heapq.heappop(q1)
            #print(node)
            dist = node[0]
            pt = node[1]
            
            if pt not in visited2:
                visited2.add(pt)
                
                if pt in graph:
                    for nei in graph[pt]:
                        if nei[0] in visited2:
                            continue
                            
                        if dist + nei[1] < ans2[nei[0]]:
                            ans2[nei[0]] = dist + nei[1]
                            
                            parent2[nei[0]] = pt
                            heapq.heappush(q1,[ans2[nei[0]], nei[0]])
            
        
        final_ans1 = set()
        f1 = 0
        final_ans2 = set()
        f2 = 0
        final_ans3 = set()
        f3 = 0
        
        chain1 = []
        p1 = dest
        #print(parent1)
        while p1 in parent1 and  p1!=src1 and parent1[p1]!=-1:
            chain1.append(p1)
            p1 = parent1[p1]
        chain1.append(p1)    
        chain2 = []
        p2 = dest
        #print(parent2)
        while p2 in parent2 and p2!=src2 and parent2[p2]!=-1:
            chain2.append(p2)
            p2 = parent2[p2]
        chain2.append(p2)    
        #print(chain1, chain2)
        
        
        if chain1[-1] == src1 or chain2[-1] == src2:
            ##src1 - dest is min
            edges = set()
            cost_result = float('inf')
            
            for x in range(len(chain1)-1):
                edges.add(str(chain1[x+1]) + "," + str(chain1[x]))
                
            par_ans_1 = src1
            c = []
            
            while par_ans_1 in parent2 and par_ans_1!= src2 and parent2[par_ans_1]!=-1:
                c.append(par_ans_1)
                par_ans_1 = parent2[par_ans_1]
                
            c.append(par_ans_1)
            
            if c[-1] == src2:
                for x in range(len(c)-1):
                    edges.add(str(c[x+1]) + "," + str(c[x]))

                temp = 0
                for x in edges:
                    temp+=costs[x]
                    
                cost_result = min(cost_result, temp)
            
            print(cost_result)
            ###src2 - dest is min
            
            edges = set()
            #cost_result = float('inf')
            
            for x in range(len(chain2)-1):
                edges.add(str(chain2[x+1]) + "," + str(chain2[x]))
                
            par_ans_2 = src2
            c = []
            
            while par_ans_2 in parent1 and par_ans_2!= src1 and parent1[par_ans_2]!=-1:
                c.append(par_ans_2)
                par_ans_2 = parent1[par_ans_2]
                
            c.append(par_ans_2)
            
            if c[-1] == src1:
                for x in range(len(c)-1):
                    edges.add(str(c[x+1]) + "," + str(c[x]))

                temp = 0
                for x in edges:
                    temp+=costs[x]
                    
                cost_result = min(cost_result, temp)
                
                
            print(cost_result)
            
            
            ##both seperate is min
            if chain1[-1] == src1 and chain2[-1] == src2:
                temp = 0
                edges = set()
                c = []

                par_ans_2 = dest
                while par_ans_2 in parent1 and  par_ans_2!= src1 and parent1[par_ans_2]!=-1:
                    c.append(par_ans_2)
                    par_ans_2 = parent1[par_ans_2]

                c.append(par_ans_2)
                for x in range(len(c)-1):
                    edges.add(str(c[x+1]) + "," + str(c[x]))
                
                c= []
                par_ans_1 = dest
                while par_ans_1 in parent2 and par_ans_1!= src2 and parent2[par_ans_1]!=-1:
                    c.append(par_ans_1)
                    par_ans_1 = parent2[par_ans_1]

                c.append(par_ans_1)
                #print(edges)
                for x in range(len(c)-1):
                    edges.add(str(c[x+1]) + "," + str(c[x]))
                    
                for x in edges:
                    temp+=costs[x]
                    
                cost_result = min(cost_result, temp)
                
                #print(cost_result)
                
                
        elif chain1[-1] != src1 and chain2[-1] != src2:
            return -1
        
        return cost_result if cost_result!=float('inf') else -1
        
        
        
   ##Solution 2(Accepted)
import heapq
class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        graph = defaultdict(list)
        
        rev_graph = defaultdict(list)
        
        for x in range(len(edges)):
            
            graph[edges[x][0]].append((edges[x][1],edges[x][2]))
            rev_graph[edges[x][1]].append((edges[x][0],edges[x][2]))
        
        def dijkstra(src,graph):
            
            ans = [float('inf') for x in range(n)]
            q =  []
            heapq.heappush(q,(0,src))
            
            ans[src] = 0
            visited = set()
            while q:
                node = heapq.heappop(q)
                
                pt = node[1]
                cost = node[0]
                
                if pt not in visited:
                    visited.add(pt)
        
                    for nei in graph[pt]:
                        if cost + nei[1] < ans[nei[0]]:
                            ans[nei[0]] = cost + nei[1]
                            heapq.heappush(q,(ans[nei[0]], nei[0]))
                       
            return ans

        ans1 = dijkstra(src1, graph)
        ans2 = dijkstra(src2, graph)
        ans3 = dijkstra(dest, rev_graph)
        
        ans = float('inf')
        
        for x in range(n):
            ans = min(ans, ans1[x] + ans2[x] + ans3[x])
            
        return ans if ans!=float('inf') else -1
                
            
