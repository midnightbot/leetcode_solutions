##ss
class Solution:
    def kthPalindrome(self, queries: List[int], l: int) -> List[int]:
        
        ##idea 1-> just find the querieth number in left healf
        ## solve for left half ans = left-half + left-half[::-1]
        
        
        ans = [-1 for x in range(len(queries))]
        
        c = 10 ** ((l-1)//2)
        cnext = 10 ** ((l-1)//2 + (1))
        for x in range(len(queries)):
            temp = queries[x]-1 + c
            temp = str(temp)
            if l%2 == 0:
                result = temp + temp[::-1]
                
            else:
                result = temp + temp[0:-1][::-1]
                
            ans[x] = int(result) if queries[x]-1 <= cnext - c - 1 else -1
        return ans
