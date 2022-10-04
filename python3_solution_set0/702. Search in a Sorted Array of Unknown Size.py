##ss
## Simple binary search
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        left = 0
        right = pow(10,4)
        
        while left <= right:
            
            mid = left + (right - left) // 2
            #print(mid)
            if reader.get(mid) == pow(2,31)-1:
                right = mid - 1
                
            elif reader.get(mid) > target:
                right = mid - 1
                
            elif reader.get(mid) == target:
                return mid
            else:
                left = mid + 1
                
        return -1       
        
