##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        
        ##find lowest common ancestor --> q. 236
        
        ##find distance of both from lowest common ancestor
        ##return sum of both
        nodes = [p,q]
        ans = self.lca(root,nodes)
        #print(ans)
        
        que = [(ans,0)]
        pdist = -1
        qdist = -1
        while que:
            node = que.pop(0)
           # print(node[0].val)
            if pdist!=-1 and qdist!=-1:
                return pdist + qdist
            if node[0].val == p:
                pdist = node[1]
                
            if node[0].val == q:
                qdist = node[1]
                
            if node[0].left:
                que.append((node[0].left,node[1]+1))
                
            if node[0].right:
                que.append((node[0].right,node[1]+1))
        
        print(pdist,qdist)
        return pdist + qdist
                
    def lca(self,root,nodes):
        
        if root == None:
            return None
        
        elif root.val in nodes:
            return root
        
        left = self.lca(root.left,nodes)
        right = self.lca(root.right,nodes)
        
        if left and right:
            return root
        
        elif left:
            return left
        elif right:
            return right

        
