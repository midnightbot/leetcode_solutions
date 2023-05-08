func rowAndMaximumOnes(mat [][]int) []int {
    ans := []int {}
    maxs := -1
    for indx,val := range mat{
        cnt := count_one(val)
        if cnt > maxs {
            ans = append(ans, indx)
            ans = append(ans, cnt)
            maxs = cnt
        }
    }
    n := len(ans)
    return []int{ans[n-2], ans[n-1]}
}

func count_one(arr []int) int{
    result := 0

    for _,val := range arr{
        if val == 1{
            result++
        }

    }
    return result
}
