class Solution:
    def countTriplets(self, arr: List[int]) -> int:

        ## choose (i,k) such that XOR arr[i] .. arr[k] == 0

        ans = 0


        for x in range(len(arr)-1):
            temp = arr[x]
            for y in range(x+1, len(arr)):
                temp^=arr[y]
                if temp == 0:
                    ans+=(y-x)
        return ans
