# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode()
        temp = ans
        while(l1 and l2):
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
                
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
                
        if l1:
            temp.next = l1
            
        if l2:
            temp.next = l2
            
        return ans.next
        
