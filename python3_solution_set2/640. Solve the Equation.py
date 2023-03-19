class Solution:
    def solveEquation(self, equation: str) -> str:
        
        def find_coeff_x(arr):
            res = 0
            t = []

            for it in arr:
                temp = it.split("x")
                temp[1] = '1'
                if len(temp[0]) == 1 and temp[0] == '+':
                    temp[0] = '1'
                if len(temp[0]) == 1 and temp[0] == '-':
                    temp[0] = '-1'
                #print(temp)
                temp = int(temp[0]) * int(temp[1])
                t.append(temp)
            return sum(t)
        def break_in_terms(s):
            arr = []
            n = len(s)
            sign = '+'
            curr = ''
            for x in range(n):
                #print(x, arr)
                if s[x] in '1234567890x':
                    curr+=s[x]

                elif s[x] in '+-':
                    if sign == '+':
                        if curr!='':
                            arr.append('+'+curr)
                    else:
                        if curr!='':
                            arr.append('-' + curr)
                    sign = s[x]
                    curr = ''

            if curr!='':
                if sign == '+':
                    arr.append('+'+curr)
                else:
                    arr.append('-'+curr)
            return arr
        parts = equation.split("=")
        
        temp1 = break_in_terms(parts[0])
        temp2 = break_in_terms(parts[1])

        #print(temp1, temp2)

        left = [] ## bring all x to left
        right = [] ## everything else to right

        for it in temp1:
            if 'x' in it:
                left.append(it)
            else:
                if it[0] == '+':
                    right.append('-'+it[1:])
                else:
                    right.append('+'+it[1:])

        for it in temp2:
            if 'x' in it:
                if it[0] == '-':
                    left.append('+' + it[1:])
                else:
                    left.append('-' + it[1:])
            else:
                right.append(it)

        #print(left,right,temp1,temp2, 'this')

        #return ''
        right_ans = sum([int(x) for x in right])
        x_coeff = find_coeff_x(left)
        #print(right_ans, x_coeff)
        if right_ans == x_coeff == 0:
            return "Infinite solutions"
        elif right_ans!=0 and x_coeff == 0:
            return "No solution"
        else:
            return 'x='+str(right_ans//x_coeff)
        #return ''
