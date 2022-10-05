# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        self.ans = 0
        
        def find_ans(prev,root,d, i):
            
            if d == depth:
                self.ans+=1
                new_node = TreeNode()
                new_node.val = val
                if i%2==0:
                    new_node.left = prev.left
                
                else:
                    new_node.right = prev.right
                
                return new_node
                
            else:
                new_node = TreeNode()
                if root is not None:
                    new_node.val = root.val

                    new_node.left = find_ans(root,root.left, d+1, 0)
                    new_node.right = find_ans(root, root.right, d+1, 1)
                    return new_node
        
        if depth == 1:
            ## new level is the top level
            new_node = TreeNode()
            new_node.val = val
            new_node.left = root
            return new_node
        
        k = find_ans(root,root,1,0)  
        
        if self.ans == 0:
            ## to add a new level below current roots
            d = 1
            q = [root]
            while d != depth - 1:
                new_q = []
                
                for x in q:
                    if x.left:
                        new_q.append(x.left)
                        
                    if x.right:
                        new_q.append(x.right)
                        
                q = new_q
                d+=1
            new_node = TreeNode()
            new_node.val = val
            for nds in q:
                nds.left = new_node
                nds.right = new_node

            return root 
        
        else:
            return k
            
        
        
        
