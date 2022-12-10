# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        mods = 10**9 + 7

        ## replace every root val by sum of the tree below it
        def make_comp(root):
            if root is None:
                return 0
            else:
                root.val+= make_comp(root.left) + make_comp(root.right)
                return root.val
        
        make_comp(root)
        q = []
        if root.left:
            q.append(root.left)
        if root.right:
            q.append(root.right)

        ## now just break every edge and see the product of the two trees
        ans = 0
        full_sum = root.val
        while q:
            new_q = []
            for x in q:
                ans = max(ans, (full_sum - x.val) * x.val)
                if x.left:
                    new_q.append(x.left)
                if x.right:
                    new_q.append(x.right)
            q = new_q
            
        return ans%mods
