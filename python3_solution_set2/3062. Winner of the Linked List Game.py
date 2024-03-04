# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        a = 0
        b = 0


        while head:
            if head.val > head.next.val:
                a+=1
            else:
                b+=1
            head = head.next.next

        return "Odd" if b > a else "Tie" if a == b else "Even"
        
