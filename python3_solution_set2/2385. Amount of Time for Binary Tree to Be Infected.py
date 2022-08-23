# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        g = {}
        edges = []
        self.cnt = 0
        def find_ans(root):
            self.cnt+=1
            if root.left:
                edges.append([root.val,root.left.val])
                find_ans(root.left)
                
            if root.right:
                edges.append([root.val,root.right.val])
                find_ans(root.right)
                
        find_ans(root)
        
        for x,y in edges:
            if x not in g:
                g[x] = [y]
            else:
                g[x].append(y)
                
            if y not in g:
                g[y] = [x]
            else:
                g[y].append(x)
                
        seen = 1
        mins = 0
        visited = set()
        q = [start]
        while seen!=self.cnt:
            mins+=1
            for x in range(len(q)):
                top = q.pop(0)
                if top not in visited:
                    visited.add(top)
                    for nei in g[top]:
                        if nei not in visited:
                            seen+=1
                            q.append(nei)
            
        return mins
