##ss
##Solution 1(Linear Search in get function) Time Limit Exceeded
class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [[[0]] for x in range(length)]
        #self.snap_id = -1
        self.snap_id = 0
        #print(self.arr)

    def set(self, index: int, val: int) -> None:
        #self.arr[index].append(val)
        thiselem = self.arr[index][-1]
        if len(thiselem) == 1:
            self.arr[index][-1] = [val]
            
        else:
            self.arr[index].append([val])
        
        #print(self.arr)

    def snap(self) -> int:
        for x in range(len(self.arr)):
            if len(self.arr[x][-1]) == 1:
                self.arr[x][-1] = [self.arr[x][-1][0],self.snap_id]
                
            #else:
                #self.arr[x].append([self.arr[x][-1][0],self.snap_id])
                
        self.snap_id+=1
        return self.snap_id-1
                

    def get(self, index: int, snap_id: int) -> int:
        #print(self.arr)
        if snap_id >= self.snap_id:
            return 0
        for x in range(len(self.arr[index])):
            if len(self.arr[index][x])==2 and self.arr[index][x][1] == snap_id:
                return self.arr[index][x][0]
            
            elif len(self.arr[index][x])==2 and self.arr[index][x][1] > snap_id:
                return self.arr[index][x-1][0]
            elif len(self.arr[index][x])==1:
                return self.arr[index][x-1][0]
        return self.arr[index][-1][0]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)


##Solution 2(Binary search in get function)
class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [[[-1,0]] for x in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.arr[index].append([self.snap_id,val])
        

    def snap(self) -> int:
        self.snap_id+=1
        return self.snap_id-1
        

    def get(self, index: int, snap_id: int) -> int:
        indx = bisect.bisect(self.arr[index],[snap_id+1])-1
        return self.arr[index][indx][1]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
