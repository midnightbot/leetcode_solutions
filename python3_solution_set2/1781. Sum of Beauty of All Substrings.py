class Solution:
    def beautySum(self, s: str) -> int:


        ## simple prefix sum concept
        
        def find_ans(arr):
            c = []
            for x in arr:
                if x!=0:
                    c.append(x)
            if len(c) <=1:
                return 0
            #print(arr)
            return max(c) - min(c)

        def find_arr(i,j):
            res = []
            for x in range(26):
                res.append(temp[j][x] - temp[i-1][x])

            return find_ans(res)

        n = len(s)  
        temp = []

        result = 0
        ans = [0 for x in range(26)]
        temp.append(copy.deepcopy(ans))

        for x in range(n):
            ans[ord(s[x]) - ord('a')]+=1
            temp.append(copy.deepcopy(ans))

        for x in range(1,n+1):
            for y in range(x+1,n+1):
                #print(s[x-1:y])
                result+=find_arr(x,y)
                #print(result)

        return result
