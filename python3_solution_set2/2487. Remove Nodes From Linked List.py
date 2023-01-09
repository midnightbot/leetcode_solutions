# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []

        while head:
            arr.append(head.val)
            head = head.next

        arr = arr[::-1]

        stack = []

        for x in arr:
            if len(stack) == 0:
                stack.append(x)

            elif stack[-1] <= x:
                stack.append(x)

        stack = stack[::-1]
        n = len(stack)


        def make_ll(i):
            if i == n:
                return None

            else:
                new_node = ListNode()
                new_node.val = stack[i]
                new_node.next = make_ll(i+1)
                return new_node

        ans = make_ll(0)

        return ans
        
