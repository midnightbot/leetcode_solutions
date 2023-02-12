class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:

        sums = sum(arr)
        if sums%3!=0:
            return False

        part_sum = sums//3

        n = len(arr)
        i = 1
        temp1 = arr[0]
        while i < n and temp1!=part_sum:
            temp1+=arr[i]
            i+=1
        #print('here', temp1, part_sum)
        if temp1!=part_sum or i ==n:
            return False
        #print('here')
        temp2 = arr[i]
        i+=1
        while i < n and temp2!=part_sum:
            temp2+=arr[i]
            i+=1
        
        if temp2!=part_sum or i ==n:
            return False

        temp3 = arr[i]
        i+=1 

        while i < n and temp3!=part_sum:
            temp3+=arr[i]
            i+=1

        return temp3==part_sum
        
