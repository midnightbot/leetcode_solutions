class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        ans1 = [float('inf') for x in range(n)]
        ans2 = [float('inf') for x in range(n)]
        
        def find_ans(ans, node):
            q = node
            step = 0
            while q!=-1:
                if ans[q]!=float('inf'):
                    break
                ans[q] = step
                step+=1
                q = edges[q]
                
            
        
        
        
            
        find_ans(ans1,node1)
        find_ans(ans2,node2)
        
        result = float('inf')
        ans_node = -1
        
        for x in range(n):
            t = max(ans1[x],ans2[x])
            if t < result:
                result = t
                ans_node = x
        
        return ans_node
        
        
