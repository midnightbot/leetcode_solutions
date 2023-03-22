class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        
        n = len(code)
        temp = code + code + code

        ans = []
        for x in range(n,2*n):
            if k > 0:
                sums = 0
                for it in range(k):
                    sums+= temp[x+it]
                ans.append(sums)
            elif k == 0:
                ans.append(0)

            elif k < 0:
                #print('here', temp)
                sums = 0
                for it in range(abs(k)):
                    sums+= temp[x-it]
                ans.append(sums)
                print(ans)
        if k > 0:
            return ans[1:] + [ans[0]]
        elif k < 0:
            return [ans[-1]] + ans[0:-1] 

        else:
            return ans
