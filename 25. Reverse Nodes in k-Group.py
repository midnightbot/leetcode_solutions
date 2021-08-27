# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        temp = []
        
        while head:
            temp.append(head.val)
            head = head.next
            
        ans = []
        tempo = []
        steps = len(temp) // k
        #print(steps)
        start = 0
        end = k
        for x in range(steps):
            tempo = temp[start : end]
            tempo = tempo[::-1]
            start+=k
            end+=k
            for y in range(k):
                ans.append(tempo[y])
        
        for x in range(steps*k, len(temp)):
            ans.append(temp[x])
        #print(ans)
        
        final = done = ListNode()
        
        for x in ans:
            done.next = ListNode(x)
            done = done.next
            
        return final.next
        
