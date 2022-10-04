class Solution:
    def minimumSum(self, num: int) -> int:
        
        a = [int(x) for x in str(num)]
        #print(a)
        a = sorted(a)
        #print(a)
        return int(str(a[0])+str(a[2])) + int(str(a[1])+str(a[3]))
