class MyLinkedList:

    def __init__(self):
        self.arr = []
        

    def get(self, index: int) -> int:
        if index < len(self.arr):
            return self.arr[index]
        return -1
        

    def addAtHead(self, val: int) -> None:
        self.arr = [val] + self.arr
        

    def addAtTail(self, val: int) -> None:
        self.arr.append(val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < len(self.arr):
            self.arr = self.arr[:index] + [val] + self.arr[index:]
        elif index == len(self.arr):
            self.arr.append(val)
        

    def deleteAtIndex(self, index: int) -> None:
        if index < len(self.arr):
            self.arr = self.arr[:index] + self.arr[index+1:]
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
