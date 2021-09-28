class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        previous = ListNode(0)
        previous.next = head
        
        prev, curr = previous, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        
        return previous.next
