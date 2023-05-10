func kItemsWithMaximumSum(numOnes int, numZeros int, numNegOnes int, k int) int {
    ans := 0
    arr := []int{}

    for x:=0;x<numOnes;x++{
        arr = append(arr, 1)
    }
    for x:=0;x<numZeros;x++{
        arr = append(arr, 0)
    }
    for x:=0;x<numNegOnes;x++{
        arr = append(arr, -1)
    }
    for x:=0;x<k;x++{
        ans+=arr[x]
    }
    return ans 
}
