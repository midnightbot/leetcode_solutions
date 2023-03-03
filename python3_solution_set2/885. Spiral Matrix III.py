class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:

        seen = set()
        result = []

        def valid(r,c):
            return 0<=r<rows and 0<=c<cols

        def find_iterator(r,c, size):
            ans = []
            ## 2*size + 1

            ## move right
            if valid(r,c) and (r,c) not in seen:
                seen.add((r,c))
                ans.append([r,c])

            for it in range(2*size-1):
                c+=1
                if valid(r,c) and (r,c) not in seen:
                    seen.add((r,c))
                    ans.append([r,c])

            ## move down
            for it in range(2*size-1):
                r+=1
                if valid(r,c) and (r,c) not in seen:
                    seen.add((r,c))
                    ans.append([r,c])

            ## move left
            for it in range(2*size):
                c-=1
                if valid(r,c) and (r,c) not in seen:
                    seen.add((r,c))
                    ans.append([r,c])

            ## move up
            for it in range(2*size):
                r-=1
                if valid(r,c) and (r,c) not in seen:
                    seen.add((r,c))
                    ans.append([r,c])

            return r,c,ans

        i = 1
        while len(result)!=rows*cols:
            rStart, cStart, temp = find_iterator(rStart, cStart, i)
            i+=1
            #print(temp)
            for it in temp:
                result.append(it)

        #print(result)
        return result

        
