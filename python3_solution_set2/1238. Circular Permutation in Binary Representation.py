class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        
        temp = []

        for x in range(1<<n):
            temp.append(start ^ x^x>>1)

        #print(temp)
        return temp
