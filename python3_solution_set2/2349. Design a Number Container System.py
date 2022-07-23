##ss
from sortedcontainers import SortedList
class NumberContainers:

    def __init__(self):
        self.maps = {}
        self.pos = {}
        

    def change(self, index: int, number: int) -> None:
        if index not in self.maps:
            self.maps[index] = number
        else:
            temp = self.maps[index]
            
            self.pos[temp].remove(index)
            self.maps[index] = number
        
        if number in self.pos:
            self.pos[number].add(index)
        else:
            self.pos[number] = SortedList()
            self.pos[number].add(index)
        #print(index,number)
        #print(self.maps,self.pos)
        #print("----")
    def find(self, number: int) -> int:
        if number in self.pos and len(self.pos[number])>0:
            return self.pos[number][0]
        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
