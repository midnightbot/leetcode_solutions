# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        ans = set()
        
        def make_new_tree(root):
            if root.left is None:
                ans.add(root.val)
                return root.val
            else:
                root.val = min(make_new_tree(root.left), make_new_tree(root.right))
                ans.add(root.val)
                return root.val
        
        make_new_tree(root)
        ans = sorted(list(ans))
        #print(ans)
        return ans[1] if len(ans) >= 2 else -1
        
