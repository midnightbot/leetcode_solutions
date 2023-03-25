class Solution:
    def splitString(self, s: str) -> bool:

        ans = []
        n = len(s)

        def find_ans(indx, curr, prev):
            if indx == n:
                if curr!='' and prev!='':
                    if int(prev)-1 == int(curr):
                        print(prev, curr)
                        ans.append(True)

            else:
                ## part of this string
                find_ans(indx+1, curr+s[indx], prev)

                ## new string
                if curr!='' and prev!='':
                    if int(prev)-1 == int(curr):
                        find_ans(indx+1, s[indx], curr)


        for x in range(n):
            find_ans(x,'',s[:x])

        return True in ans
