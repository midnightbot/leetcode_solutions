class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ##[1,4,2,3]
        ##[1,2,4,3]
        ##[3,4,2,1]
        ##[4,3,2,1]

        ## find the current max number, bring it to the first position and then its respective position, continue this till the array is sorted

        temp = sorted(arr, reverse = True)
        ans =[] 
        i = 0
        n = len(temp)

        while i < n:
            
            indx = arr.index(temp[i])
            #print(i, arr, indx, temp[i]-1)
            if indx == temp[i] - 1: ## already in correct position
                print('here')
                i+=1
                continue
            
            else:
                to_be_index = temp[i] -1
                if indx!=0:
                    ans.append(indx)
                if to_be_index!=0:
                    ans.append(to_be_index)
                arr = arr[:indx+1][::-1] + arr[indx+1:]
                
                arr = arr[:to_be_index+1][::-1] + arr[to_be_index+1:]
                i+=1
        return [x+1 for x in ans]
