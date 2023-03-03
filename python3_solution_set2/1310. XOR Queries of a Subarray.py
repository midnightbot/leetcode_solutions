class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:

        ## full XOR left XOR right
        ## kind of like simple prefix sum

        ## say a ^ b ^ c = full

        ## so to find b
        ## b = full ^ a ^ c



        def find_xor(arr):
            ans = 0
            for x in arr:
                ans^=x
            return ans

        full = find_xor(arr)
        
        pre_xor = [0]

        for x in range(len(arr)):
            pre_xor.append(pre_xor[-1]^arr[x])

        pre_xor = pre_xor[1:]
        post_xor = [0]
        for x in range(len(arr)-1,-1,-1):
            post_xor.append(post_xor[-1]^arr[x])

        post_xor = post_xor[1:]
        post_xor = post_xor[::-1]

        n = len(arr)
        ans = []
        for x,y in queries:
            ## ans = full XOR pre_xor[x-1] XOR post_xor[y+1]
            if x == 0:
                a = 0
            else:
                a = pre_xor[x-1]

            if y+1 == n:
                b = 0

            else:
                b = post_xor[y+1]

            ans.append(full ^ a ^ b)

        return ans
