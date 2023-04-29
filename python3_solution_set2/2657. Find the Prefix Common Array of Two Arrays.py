class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        def check_overlap(dicts):
            cnt = 0
            for x in dicts:
                if dicts[x]%2==0:
                    cnt+=1
            return cnt

        arr = []

        dicts = {}

        for x,y in zip(A,B):
            dicts[x] = dicts.get(x,0) + 1
            dicts[y] = dicts.get(y,0) + 1

            arr.append(check_overlap(dicts))

        return arr
