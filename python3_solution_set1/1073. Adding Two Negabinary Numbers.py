##ss
class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        
        def find_num(arr):
            ans  = 0
            arr = arr[::-1]
            for c,x in enumerate(arr):
                if c%2==0:
                    ans+= (2 ** c) * x 
                else:
                    ans-= (2**c) * x
                
            
            return ans
        
        def convert(num):
            
            if num == 0:
                return [0]
            
            else:
                ans = []
                while num!=0:
                    num, remainder = divmod(num, -2)
                    if remainder < 0:
                        num, remainder = num + 1, remainder + 2
                    ans.append(int(remainder))
                return ans[::-1]
            
        return convert(find_num(arr1) + find_num(arr2))
        
