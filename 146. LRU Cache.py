##ss
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dicts = {}
        self.arr = []
        self.count = 0

    def get(self, key: int) -> int:
        

        if key in self.dicts.keys():
            self.arr.remove(key)
            self.arr.append(key)
            return self.dicts[key]
        
        else:
            #self.arr.append(key)
            return -1
        

    def put(self, key: int, value: int) -> None:
        #print(self.arr)
        
        if key in self.dicts.keys():
                self.dicts[key] = value
                self.arr.remove(key)
                
        elif self.count < self.capacity and key not in self.dicts.keys():
                self.dicts[key] = value
                self.count+=1
                
        
        elif self.count == self.capacity:
            #print(self.arr,self.dicts)
            self.dicts.pop(self.arr[0])
            self.arr.remove(self.arr[0])
            self.dicts[key] = value
            

        self.arr.append(key)
                    
            
            
            
        
 
