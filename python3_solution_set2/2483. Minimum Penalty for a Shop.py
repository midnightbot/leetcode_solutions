class Solution:
    def bestClosingTime(self, customers: str) -> int:

        ## open -> no customers (open and 'N')
        ## closed -> customer  (closed and 'Y')

        ## like two pointer approach, maintain count of y and n while shop open and shop closed
        ry = customers.count("Y")
        rn = customers.count("N")
        ly = 0
        ln = 0
        hour = 0
        p = ry

        for x in range(0,len(customers)):
            if customers[x] == "Y":
                ly+=1
                ry-=1
            else:
                ln+=1
                rn-=1

            new_p = ln + ry
            #print(new_p,p)
            if new_p < p:
                p = new_p
                hour = x+1

        return hour
            

        return penalty
