# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countGreatEnoughNodes(self, root: Optional[TreeNode], k: int) -> int:

        ## simple dfs solution


        def dfs(node):
            if not node:
                return []

            arr = sorted(dfs(node.left) + dfs(node.right))[:k]

            if len(arr) >= k and arr[-1] < node.val:
                self.ans+=1

            else:
                arr.append(node.val)

            return arr

        self.ans = 0
        dfs(root)
        return self.ans
