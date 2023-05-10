class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:

        maps = {}
        n = len(words[0])
        ans = []

        ## create a map containing all prefixes, and all words with those prefixes
        for x in words:
            for y in range(1,n+1):
                curr = x[:y]
                if curr in maps:
                    maps[curr].append(x)
                else:
                    maps[curr] = [x]

        def valid(arr, i):
            '''
            Given an arr, check if the arr is valid upto i'th row and i'th column
            '''
            ## check if inserted i words are valid
            col_arr = [x for x in zip(*arr)] ## row to col transformation
            if i == 1:
                return True
            else:
                for it in range(i):
                    if "".join(arr[it])!="".join(col_arr[it]):
                        return False

                return True

        def insert(arr, wrd, i):
            '''
            Given an arr, insert the word 'wrd' in the i'th row and i'th col
            '''
            for x in range(len(wrd)):
                arr[i][x] = wrd[x]

            for x in range(len(wrd)):
                arr[x][i] = wrd[x]

            return arr

        def find_ans(arr, i, wrds):
            '''
            Recursive Function to pick one word and move on to selecting next word
            '''
            if i == n:
                ans.append(wrds)

            else:
                curr = arr[i][:i]
                curr = ''.join(curr)
                
                if curr in maps:
                    for it in maps[curr]:
                        arr = insert(arr, it, i)
                        if valid(arr, i):
                            find_ans(arr,i+1, wrds+[it])

        ## insert each word in words in the 0'th row and 0'th column and try to find a valid combination from here
        for it in words:
            arr = [['' for x in range(n)]for y in range(n)]
            arr = insert(arr, it,0)
            find_ans(arr,1,[it])
        return ans

