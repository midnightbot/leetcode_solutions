# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        paths = []
        
        def dfs(node, p):
            if node.left == None and node.right == None:
                paths.append(p+[node.val])

            else:
                if node.left:
                    dfs(node.left, p+[node.val])

                if node.right:
                    dfs(node.right, p+[node.val])

        dfs(root, [])
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        n = len(arr)

        def comp(arr1, arr2):
            
            for x in range(len(arr1) - n + 1):
                comp = arr1[x:x+n]
                if comp == arr2:
                    return True
                
            return False

        
        for it in paths:
            ans = comp(it, arr)
            if ans:
                return True

        return False
