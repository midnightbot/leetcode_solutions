##ss
class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        
        n = len(parents)
        
        child = {}
        graph = {}
        
        for x in range(len(parents)):
            if parents[x] not in graph:
                graph[parents[x]] = [x]
            else:
                graph[parents[x]].append(x)
                
        
        
        def countnodes(node):
            #print(node)
            if node in child:
                return sum(child[node])
            
            elif node not in graph:
                child[node] = [0,0]
                return 1
            
            else:
                if len(graph[node]) == 2:
                    child[node] = [countnodes(graph[node][0]),countnodes(graph[node][1])]
                else:
                    child[node] = [countnodes(graph[node][0]) , 0]
                #child[node] =  1 + (countnodes(graph[node][0]) + countnodes(graph[node][1]))
                return sum(child[node]) + 1
            
        countnodes(graph[-1][0])
        #print(child)
        ans = {}
        result = 0
        #print(child)
        
        for x in child:
            l = child[x][0]
            r = child[x][1]
            left = n - (l+r+1)
            
            ans[max(1,l) * max(1,r) * max(1,left)] = ans.get(max(1,l) * max(1,r) * max(1,left) , 0) + 1
            
            result = max(result, max(1,l) * max(1,r) * max(1,left))
            
        return ans[result]
