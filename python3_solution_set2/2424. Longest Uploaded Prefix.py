## ss
class LUPrefix:
    
    ## Union Find Template ##
    def find_parent(self,x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find_parent(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        xs = self.find_parent(x)
        ys = self.find_parent(y)
        
        if xs!=ys:
            self.parent[max(xs,ys)] = min(xs,ys)
            self.size[min(xs,ys)]+=self.size[max(xs,ys)]
            return True
        
        return False
    ## Union Find Template ##
    
    def __init__(self, n: int):
        self.arr = [0 for x in range(n+1)]
        self.parent = [x for x in range(n+1)]
        self.size = [0 for x in range(n+1)]
        self.n = n

    def upload(self, video: int) -> None:
        self.arr[video] = 1
        self.size[video] = 1
        
        if video+1 <= self.n and self.arr[video+1] == 1:
            self.union(video, video+1)
        #print(self.size, self.parent)
        if video - 1 >=0 and self.arr[video-1] == 1:
            self.union(video, video-1)
        #print(self.size, self.parent)
            
    def longest(self) -> int:
        #print(self.arr)
        #print(self.size)
        #print(self.parent)
        #print("----")
        return self.size[1]
        


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()
