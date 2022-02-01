##ss
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ##solution1 
        ##linkedlist -> array -> sorted array -> linked list
        
        ##solution 2
        ##as the elements are sorted according to their absolute values whenever we see a negative elem just bring it to the start of list
        ##time complexity : O(n)
        if head == None or head.next == None:
            return head
        root = head
        prev = head
        head = head.next
        while head!=None:
            #print(root,prev.val,head.val)
            #prev = head
            #print(root)
            if head.val < 0:
                
                nextnode = head.next
                prev.next = head.next
                head.next = root
                root = head
                #print(nextnode,root)
                
            
                head = nextnode
                
            else:
                prev = head
                head = head.next
            
            
        return root
        
