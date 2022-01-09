##ss
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ##Time complexity - O(n)
        ##space complexity - O(1)
        ##approach : divide list into 2 halves
        ##reverse 2nd half
        ##keep on finding sum on current pointers on both LL and update global max
        lens = 0
        head1 = head
        while head:
            lens+=1
            head = head.next
            
        headstart = head1
        prevs = None
        for x in range(lens//2):
            prevs = head1
            head1 = head1.next
            
        head2start = head1
        prevs.next = None
        #print(head1)
        prev = None
        while head2start:
            nextnode = head2start.next
            head2start.next = prev
            prev = head2start
            head2start = nextnode
        
        ans = -float('inf')
        while headstart:
            ans = max(ans,headstart.val + prev.val)
            headstart = headstart.next
            prev = prev.next
            
        return ans
        #print(headstart,prev)
        
        
        
