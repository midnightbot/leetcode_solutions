##ss
class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.arr = []
        for x in range(len(vec)):
            for y in range(len(vec[x])):
                self.arr.append(vec[x][y])
                
        self.pointer = 0
        

    def next(self) -> int:
        
        self.pointer+=1
        return self.arr[self.pointer-1]

    def hasNext(self) -> bool:
        
        if self.pointer == len(self.arr):
            return False
        
        else:
            return True
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
