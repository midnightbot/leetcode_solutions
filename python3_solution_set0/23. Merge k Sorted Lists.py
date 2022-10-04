# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = []
        
        for x in lists:
            head = x
            while head:
                ans.append(head.val)
                head = head.next
                
        ans = sorted(ans)
        #print(ans)
        
        final = temp = ListNode()
        
        for x in ans:
            temp.next = ListNode(x)
            temp = temp.next
        return final.next
        
