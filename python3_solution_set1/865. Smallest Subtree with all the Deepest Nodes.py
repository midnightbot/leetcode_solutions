##ss
##same as 1123. Lowest Common Ancestor of Deepest Leaves

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        parent = {}
        
        q = [root]
        deep = []
        nodes = {}
        if root.left is None and root.right is None:
            return root
        while q:
            deep = copy.deepcopy(q)
            for x in range(len(q)):
                node = q.pop(0)
                nodes[node.val] = node
                if node.left:
                    q.append(node.left)
                    parent[node.left.val] = node.val
                    
                if node.right:
                    q.append(node.right)
                    parent[node.right.val] = node.val
                    
        deep = [x.val for x in deep]     
        print(deep)
        if len(deep) == 1:
            #print("inside")
            #print(parent[deep[0]])
            return nodes[deep[0]]
        
        else:
            visited = set()
            arr = []
            
            while len(visited)!=1:
                
                deep = [parent[x] for x in deep]
                visited = set()
                for x in range(len(deep)):
                    visited.add(deep[x])
                    
            return nodes[list(visited)[0]]
        
