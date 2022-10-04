##ss
##prefix product
class ProductOfNumbers:

    def __init__(self):
        self.arr = []
        self.zeros = []
        #self.nums = []
    def add(self, num: int) -> None:
        #self.nums.append(num)
            
        if num == 0:
            self.arr.append(0)
            self.zeros.append(len(self.arr)-1)
            
        elif len(self.arr) == 0 and num!=0:
            self.arr.append(num)
            
        elif len(self.arr) >=1:
            if num == 0:
                self.zeros.append(len(self.arr))
            self.arr.append(max(self.arr[-1] * num, num))
        

    def getProduct(self, k: int) -> int:
        #print(self.nums,self.arr,k,self.zeros,len(self.arr)-k+1,-k-1)
        if self.arr[-1] == 0 or self.arr[-k] == 0 or (self.zeros and len(self.arr)-k+1 <= self.zeros[-1]):
            return 0
        
      
        if len(self.arr) >= k+ 1:
            return self.arr[-1] // max(self.arr[-k-1],1)
        
        else:
            return self.arr[-1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
