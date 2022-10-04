##ss
class ListNode:
    def __init__(self,val = -1,next=None):
        self.val = val
        self.next = next
class Skiplist:

    def __init__(self):
        self.buckets = {x:ListNode() for x in range(10)}
        

    def search(self, target: int) -> bool:
        thislist = self.buckets[int(str(target)[0])]
        vals = []
        while thislist:
            vals.append(thislist.val)
            
            if thislist.val == target:
                #print(vals,"True",target)
                return True
            
            thislist = thislist.next
            
        #print(vals,"False",target)
        return False
        

    def add(self, num: int) -> None:
        thislist = self.buckets[int(str(num)[0])]
        
        if thislist.val == -1:
            thislist.val = num
            self.buckets[int(str(num)[0])] = ListNode(num)
            
        else:
            prev = ListNode()
            while thislist and thislist.val <= num:
                prev = thislist
                thislist = thislist.next
                
            newnode = ListNode(num)
            if thislist is not None:## if element is getting added in between somewhere
                gonext = thislist.next
                thislist.next = newnode
                newnode.next = gonext
            else: ## element is getting added at the end of sorted list
                prev.next = ListNode(num)
                
            

    def erase(self, num: int) -> bool:
        
        if not self.search(num):
            return False
        
        thislist = self.buckets[int(str(num)[0])]
        if thislist.val == num:
            #thislist = thislist.next
            self.buckets[int(str(num)[0])] = thislist.next if thislist.next is not None else ListNode()
            return True
        else:
            prev = ListNode()
            while thislist.val != num:
                prev = thislist
                thislist = thislist.next
            
            gonext = thislist.next
            thislist.next = None
            prev.next = gonext
            return True

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
