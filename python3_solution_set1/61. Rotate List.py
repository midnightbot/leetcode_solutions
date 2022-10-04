##ss
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        
        if head is None or k ==0:
            return head
        og_head = head
        
        lens = 0
        
        while head!=None and head.next!=None:
            lens+=1
            head = head.next
            
        lens+=1
        
        if lens == 1:
            return head
        rotations = k % lens
        
        if rotations == 0:
            return og_head
        #print(rotations)
        
        ##move last 'rotations' number of nodes in the beginning
        
        
        ret_head = og_head
        
        c = 0
        
        while c!= lens - rotations - 1:
            og_head = og_head.next
            c+=1
            
        newh = og_head.next
        og_head.next = None
        
        it = newh
        
        while it.next!=None:
            it = it.next
            
        it.next = ret_head
        return newh
