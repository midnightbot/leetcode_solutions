##ss
class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.arr = encoding
        

    def next(self, n: int) -> int:
        #print(self.arr)
        ret_val = -1
        remove = 0
        x = 0
        
        while n!=0 and x < len(self.arr):
            if self.arr[x] > n:
                self.arr[x]-=n
                n = 0
                ret_val = self.arr[x+1]
                #return self.arr[x+1]
            
            elif self.arr[x] == n:
                self.arr[x] = 0
                ret_val = self.arr[x+1]
                remove+=1
                n = 0
                
            elif self.arr[x] < n:
                n-=self.arr[x]
                self.arr[x] = 0
                remove+=1
                
            x+=2
                
        #self.arr = self.arr[2*remove:]
        #print(self.arr)
        #print(remove)
        for y in range(remove):
            self.arr.pop(0)
            self.arr.pop(0)
            
        #print(self.arr)
        return ret_val
                
        
            
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
