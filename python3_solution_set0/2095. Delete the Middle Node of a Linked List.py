##ss
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp1 = head
        temp2 = head
        
        count = 0
        while head.next:
            head = head.next
            count+=1
        count+=1
        if count == 1:
            return head.next
        if count%2 == 0:
            mids = int(count//2) 
            
        else:
            mids = int((count-1)//2)
        
        #print(mids)
        start = 0
        prev = head
        while start!=mids:
            prev = temp1
            temp1 = temp1.next
            start+=1
            
        prev.next = temp1.next
        return temp2
        
