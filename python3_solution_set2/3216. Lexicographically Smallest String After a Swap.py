class Solution:
    def getSmallestString(self, s: str) -> str:
        arr = [int(x) for x in s]

        for x in range(1, len(arr)):
            if arr[x]%2==0 and arr[x-1]%2==0:
                if arr[x] < arr[x-1]:
                    arr[x-1],arr[x] = arr[x], arr[x-1]
                    break

            elif arr[x]%2!=0 and arr[x-1]%2!=0:
                if arr[x] < arr[x-1]:
                    arr[x-1],arr[x] = arr[x], arr[x-1]
                    break

        return "".join([str(x) for x in arr])
        
