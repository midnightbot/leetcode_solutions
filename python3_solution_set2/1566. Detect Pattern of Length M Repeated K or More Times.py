class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:

        ans = 0
        for x in range(len(arr)-m):
            if arr[x] == arr[x+m]:
                ans+=1
            else:
                ans = 0
            if ans == (k-1)*m:
                return True

        return False


                


            
