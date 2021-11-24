# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = ListNode()
        prev = temp
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        while l1!=None and l2!=None:
            if l1.val < l2.val:
                mins = l1.val
                l1 = l1.next
            else:
                mins = l2.val
                l2 = l2.next

            ans = ListNode()
            ans.val = mins
            ans.next = None
            prev.next = ans
            prev = ans
        #print(l1,l2)
        
        if l1!=None:
            ans.next = l1
            
        if l2!=None:
            ans.next = l2
            
        
        return temp.next
        
