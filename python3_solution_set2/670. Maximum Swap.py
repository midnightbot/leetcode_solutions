class Solution:
    def maximumSwap(self, num: int) -> int:
        

        ## find the digit in num which has some digit greater than it towards its right and replace this pair
        num = [x for x in str(num)]
        temp = [num[-1]]
        for x in num[::-1][1:]:
            temp.append(str(max(int(temp[-1]), int(x))))

        temp = temp[::-1]
        replace = -1
        replaced = -1
        for x in range(len(num)):
            if int(num[x]) < int(temp[x]):
                replaced = num[x]
                num[x] = temp[x]
                replace = temp[x]
                break
        
        for x in range(len(num)-1,-1,-1):
            if num[x] == replace:
                num[x] = replaced
                break

        return int("".join(num))
