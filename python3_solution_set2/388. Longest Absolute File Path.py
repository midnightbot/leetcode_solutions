class Solution:
    def lengthLongestPath(self, input: str) -> int:

        temp = input.split("\n")
        def conv(strs):
            lens = 0
            wrd = ""
            for x in range(len(strs)):
                if strs[x] == "\t":
                    lens+=1
                else:
                    wrd+=strs[x]
            return [wrd,lens]
            
        temp = [conv(x) for x in temp]
        stack = []
        ans = 0

        def find_len(arr):
            k = 0
            for it1,it2 in arr:
                k+=len(it1)
            return k + len(arr) - 1


        for name,lvl in temp:
            if len(stack) == 0:
                stack.append([name,lvl])
                if "." in name and name[-1]!=".":
                    ans = max(ans, find_len(stack))

            elif stack[-1][1] < lvl:
                stack.append([name,lvl])
                if "." in name and name[-1]!=".":
                    ans = max(ans, find_len(stack))

            elif stack[-1][1] >= lvl:
                while stack and stack[-1][1] >= lvl:
                    stack.pop()
                    if stack and "." in stack[-1][0] and stack[-1][0]!=".":
                        ans = max(ans, find_len(stack))
                stack.append([name,lvl])
                if "." in stack[-1][0] and stack[-1][0][-1]!=".":
                    ans = max(ans, find_len(stack))



        if "." in stack[-1][0] and stack[-1][0][-1]!=".":
            ans = max(ans, find_len(stack))
        return ans

        
