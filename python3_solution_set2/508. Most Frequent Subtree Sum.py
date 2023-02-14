# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:

        ans = {}

        def find_ans(node):
            if node is None:
                return 0

            elif node.left is None and node.right is None:
                ans[node.val] = ans.get(node.val,0) + 1
                return node.val

            else:
                node.val+= find_ans(node.left) + find_ans(node.right)
                ans[node.val] = ans.get(node.val,0) + 1
                return node.val

        
        find_ans(root)
        maxs = max(list(ans.values()))
        result = []

        for x in ans:
            if ans[x] == maxs:
                result.append(x)

        return result
