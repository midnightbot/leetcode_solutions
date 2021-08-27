# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = []
        
        while head:
            temp.append(head.val)
            head = head.next
            
        #print(temp)
        temp2 = []
        removed = []
        for x in temp:
            if x not in temp2 and x not in removed:
                #print("inside")
                temp2.append(x)
                #print(temp2)
            elif x in temp2:
                temp2.remove(x)
                removed.append(x)
            #print(temp2)
                
            
            
        final = ans = ListNode()
        
        for x in temp2:
            ans.next = ListNode(x)
            ans = ans.next
            
        return final.next
        
