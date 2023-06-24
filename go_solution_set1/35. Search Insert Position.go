func searchInsert(nums []int, target int) int {
    for indx, num := range nums{
        if num == target{
            return indx
        }
        if num > target {
            return indx
        } 
    }
    return len(nums)
}
