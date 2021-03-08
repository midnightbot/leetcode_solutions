class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        digits = []
        ans = []
        counter =0
        for x in range(left,right+1,1):
            digits = [int(d) for d in str(x)]
            if len(digits)==1:
                ans.append(digits[0])
                
            elif 0 not in digits:
                counter = 0
                for y in digits:
                    if x%y!=0:
                        break
                    counter+=1
                    if counter==len(digits):
                        ans.append(x)
        return ans
                
        
