##ss
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        
        self.nums1 = nums1
        self.nums2 = nums2
        self.dicts = {}
        self.dicts1 = {}
        for x in range(len(self.nums2)):
            if self.nums2[x] in self.dicts:
                self.dicts[self.nums2[x]]+=1
                
            else:
                self.dicts[self.nums2[x]] = 1
                
        for x in range(len(self.nums1)):
            if self.nums1[x] in self.dicts1:
                self.dicts1[self.nums1[x]]+=1
                
            else:
                self.dicts1[self.nums1[x]] = 1
        

    def add(self, index: int, val: int) -> None:
        
        oldnum = self.nums2[index]
        self.nums2[index]+=val
        newnum = self.nums2[index]
        
        self.dicts[oldnum]-=1
        
        if newnum in self.dicts:
            self.dicts[newnum]+=1
            
        else:
            self.dicts[newnum] = 1
        

    def count(self, tot: int) -> int:
        
        ans = 0
        visited = set()
        #print(self.nums1,self.nums2,tot,self.dicts1,self.dicts)
        for x in self.dicts1:
            if tot - x in self.dicts:
                ans+= self.dicts1[x] * self.dicts[tot - x]
                
        return ans
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
