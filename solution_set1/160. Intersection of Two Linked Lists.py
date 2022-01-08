# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        len1 = 0
        len2 = 0
        head1 = headA
        head2 = headB
        while headA!=None:
            len1+=1
            headA = headA.next
            
        while headB!=None:
            len2+=1
            headB = headB.next
            
        if len1==len2:
            return self.match(head1,head2)
        
        elif len1 > len2:
            diff = len1 - len2
            for x in range(diff):
                head1 = head1.next
                
            return self.match(head1,head2)
        
        elif len1 < len2:
            diff = len2 - len1
            for x in range(diff):
                head2 = head2.next
                
            return self.match(head1,head2)
            
    def match(self,head1,head2):
        
        while head1:
            if head1 == head2:
                return head1
            head1 = head1.next
            head2 = head2.next
            
        return None
        
