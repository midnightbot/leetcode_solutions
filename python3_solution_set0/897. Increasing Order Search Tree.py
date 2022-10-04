##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        ans = []
        queue = [root]
        
        while queue:
            node = queue.pop(0)
            ans.append(node.val)
            if node.left:
                queue.append(node.left)
                
            if node.right:
                queue.append(node.right)
                
        ans = sorted(ans)
        finals = None
        for x in range(len(ans)-1,-1,-1):
            #print("finals")
            new_node = TreeNode()
            new_node.val = ans[x]
            new_node.right = finals
            #print(new_node)
            new_node.left = None
            finals = new_node
            
        return finals
            
            
        
