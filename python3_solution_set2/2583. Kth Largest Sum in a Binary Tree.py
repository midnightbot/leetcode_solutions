# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

        arr = []

        q = [root]

        while q:
            temp = 0
            new_q = []
            for x in q:
                temp+=x.val

                if x.left:
                    new_q.append(x.left)
                if x.right:
                    new_q.append(x.right)

            arr.append(temp)
            q = new_q

        arr = sorted(arr, reverse=True)
        #print(arr)
        if len(arr) < k:
            return -1
        return arr[k-1]
