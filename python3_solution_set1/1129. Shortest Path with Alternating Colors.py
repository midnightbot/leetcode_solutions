##ss
class Solution:
    def shortestAlternatingPaths(self, n: int, r: List[List[int]], b: List[List[int]]) -> List[int]:
        
        ans = [-1 for x in range(n)]
        
        ans[0] = 0
        rg = {x:[] for x in range(n)}
        bg = {x:[] for x in range(n)}
        
        for x in r:
            rg[x[0]].append(x[1])
            
        for x in b:
            bg[x[0]].append(x[1])
            
        #print(rg,bg)
            
        def do_bfs(node,reach,color):
            #print("inside")
            q = [(node,color)]
            visited = set()
            visited.add((node,color))
            while q:
                top = q.pop(0)
                thisnode = top[0]
                thiscolor = top[1]
                #print(q,thisnode,thiscolor[-1])
                if thisnode == reach:
                    return len(thiscolor) - 1
                
                else:
                    if thiscolor[-1] == 'r':
                        for nei in bg[thisnode]:
                            if (nei,'b') not in visited: 
                                q.append((nei, thiscolor + 'b'))
                                visited.add((nei,'b'))
                            
                    else:
                        for nei in rg[thisnode]:
                            if (nei, 'r') not in visited:
                                visited.add((nei,'r'))
                                q.append((nei, thiscolor + 'r'))
                            
            return -1
                            
                            
        #do_bfs(0,x,'b')
        #return []
        for x in range(1,len(ans)):
            t1 = do_bfs(0,x,'r')
            t2 = do_bfs(0,x,'b')
            #print(t1,t2)
            if t1 == -1 and t2!=-1:
                ans[x] = t2
                
            elif t2 == -1 and t1!=-1:
                ans[x] = t1
                
            elif t1!=-1 and t2!=-1:
                ans[x] = min(t1,t2)
                
        return ans
        
        
