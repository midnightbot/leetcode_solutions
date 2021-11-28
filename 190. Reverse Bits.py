class Solution:
    def reverseBits(self, n: int) -> int:
        
        binary_number ='{:032b}'.format(n)
        ans = [int(x) for x in str(binary_number)]
        #ans = ans[::-1]
        print(ans)
        nums = 0
        for x in range(len(ans)):
            nums+= ans[x] * pow(2,x) 
        
        return nums
        
