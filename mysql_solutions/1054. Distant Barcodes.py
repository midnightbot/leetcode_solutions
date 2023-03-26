class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        
        n = len(barcodes)

        temp = Counter(barcodes)
        arr = [[x,temp[x]] for x in temp]
        arr = sorted(arr, key = lambda x:(-x[1]))
        barcodes = []

        for num,rep in arr:
            barcodes+=[num for it in range(rep)]

        #return []
        i=0
        ans = [0 for x in range(n)]
        for x in range(0,n,2):
            ans[x] = barcodes[i]
            i+=1

        for x in range(1,n,2):
            ans[x] = barcodes[i]
            i+=1
        return ans
