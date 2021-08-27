# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        temp = []
        while head:
            temp.append(head.val)
            head = head.next
            
        del temp[len(temp) - n]
        #print(temp)
        final = ans = ListNode()
        for x in temp:
            ans.next = ListNode(x)
            ans = ans.next
            
        return final.next
            

            
        
