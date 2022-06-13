# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        leaf_nodes = set()
        
        q = [root]
        visited = set()
        #visited.add(root)
        conn = {}
        
        while q:## finding all the leaf nodes and also finding all the connections to travel during bfs
            top = q.pop(0)
            
            if top.left==None and top.right == None:
                leaf_nodes.add(top)
                
            else:
                if top.left:
                    if top not in conn:
                        conn[top] = [top.left]
                        
                    else:
                        conn[top].append(top.left)
                        
                    if top.left not in conn:
                        conn[top.left] = [top]
                    else:
                        conn[top.left].append(top)
                    q.append(top.left)
                    
                if top.right:
                    if top not in conn:
                        conn[top] = [top.right]
                        
                    else:
                        conn[top].append(top.right)
                        
                    if top.right not in conn:
                        conn[top.right] = [top]
                    else:
                        conn[top.right].append(top)
                    q.append(top.right)
                    
        
        
        def do_bfs(node):## start bfs from a leaf node and go d uptil d steps and see if you find any other leaf node.
            
            q = [node]
            steps = 0
            seen = set()
            pairs = 0
            seen.add(node)
            while q and steps < distance:
                
                for x in range(len(q)):
                    top = q.pop(0)
                    
                    if top!=node and top in leaf_nodes:
                        pairs+=1
                    
                    if top in conn:
                        for nei in conn[top]:
                            if nei not in seen:
                                seen.add(nei)
                                q.append(nei)

                steps+=1
                #print(q,steps)
            for x in q:
                if x in leaf_nodes:
                    pairs+=1
                    
            return pairs
        
        ans  = 0
        
        for x in leaf_nodes:
            ans+= do_bfs(x)
            
        return ans//2 ## pairs will be counted twice (4,3) (3,4) but both are same
        
