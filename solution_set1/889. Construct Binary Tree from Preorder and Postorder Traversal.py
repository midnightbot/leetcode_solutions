##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        #self.visited = set()
        return self.make_tree(preorder,postorder)
    
    def make_tree(self,preorder,postorder):
        
        if len(preorder) == 0:
            return 
        node = TreeNode(preorder[0])
        preorder = preorder[1:]
        postorder = postorder[:-1]
        
        if len(preorder) == 0:
            return node
        #print(preorder,postorder)
        i = postorder.index(preorder[0])
        node.left = self.make_tree(preorder[:i+1],postorder[:i+1])
        node.right = self.make_tree(preorder[i+1:],postorder[i+1:])
        
        return node
        
        
        
        
