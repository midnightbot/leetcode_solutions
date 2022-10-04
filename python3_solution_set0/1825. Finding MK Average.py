##ss
##Approach1 (Time Limit Exceeded)
## Here will finding insert index, I am using linear time
##which can be improved to logarithmic time using binary search (using bisect libraray)
class MKAverage:

    def __init__(self, m: int, k: int):
        self.arr = []
        self.full = []
        self.sum = 0
        self.m = m
        self.k = k
        self.pointer = 0

    def addElement(self, num: int) -> None:
        
        if len(self.arr) < self.m:
            var = False
            for x in range(len(self.arr)):
                
                if self.arr[x] >= num:
                    var = True
                    self.arr.insert(x,num)
                    break
                    
            if var == False:
                self.arr.append(num)
                
            self.full.append(num)
            
            if len(self.arr) == self.m:
                self.sum = sum(self.arr[self.k:self.m-self.k])
                
        
        else:
            #print(self.pointer,self.full)
            indx = self.arr.index(self.full[self.pointer])
            
            if indx < self.k:
                self.sum-=self.arr[self.k]
                
            elif indx >= self.m - self.k:
                self.sum -= self.arr[self.m-self.k-1]
                
            else:
                self.sum-=self.full[self.pointer]
                
            self.arr.pop(indx)
            
            ##adding new elem to list
            var = False
            pos  = 0
            for x in range(len(self.arr)):
                if self.arr[x] >= num:
                    var = True
                    pos = x
                    self.arr.insert(x,num)
                    break
                    
            if var == False:
                pos = len(self.arr)
                self.arr.append(num)
                
            if pos < self.k:
                self.sum+=self.arr[self.k]
                
                
            elif pos >= self.m - self.k:
                self.sum+=self.arr[self.m-self.k-1]
                
            else:
                self.sum+= num
                
            self.pointer+=1
            self.full.append(num)
                    
        

    def calculateMKAverage(self) -> int:
        #print(self.arr)
        if len(self.arr) < self.m:
            return -1 
        
        else:
            return self.sum // (self.m - 2 * self.k)
        


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()


## Approach 2 (Accepted)
import bisect
class MKAverage:

    def __init__(self, m: int, k: int):
        self.arr = []
        self.full = []
        self.sum = 0
        self.m = m
        self.k = k
        self.pointer = 0

    def addElement(self, num: int) -> None:
        
        if len(self.arr) < self.m:
            var = False
            indx = bisect.bisect_right(self.arr,num)
            self.arr.insert(indx,num)
                
            self.full.append(num)
            
            if len(self.arr) == self.m:
                self.sum = sum(self.arr[self.k:self.m-self.k])
                
        
        else:
            #print(self.pointer,self.full)
            indx = bisect.bisect_left(self.arr,self.full[self.pointer])
            #indx = self.arr.index(self.full[self.pointer])
            
            if indx < self.k:
                self.sum-=self.arr[self.k]
                
            elif indx >= self.m - self.k:
                self.sum -= self.arr[self.m-self.k-1]
                
            else:
                self.sum-=self.full[self.pointer]
                
            self.arr.pop(indx)
            
            ##adding new elem to list
            var = False
            pos  = bisect.bisect_right(self.arr,num)
            
            self.arr.insert(pos,num)
                
            if pos < self.k:
                self.sum+=self.arr[self.k]
                
                
            elif pos >= self.m - self.k:
                self.sum+=self.arr[self.m-self.k-1]
                
            else:
                self.sum+= num
                
            self.pointer+=1
            self.full.append(num)
                    
        

    def calculateMKAverage(self) -> int:
        #print(self.arr)
        if len(self.arr) < self.m:
            return -1 
        
        else:
            return self.sum // (self.m - 2 * self.k)
        


