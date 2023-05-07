func minNumber(nums1 []int, nums2 []int) int {
    sort.Ints(nums1)
    sort.Ints(nums2)

    for _, val := range nums1{
        if has_element(nums2, val){
            return val
        }
    }

    if nums1[0] > nums2[0]{
        return nums2[0]*10 + nums1[0]
    } else {
        return nums2[0] + nums1[0]*10
    }
}

func has_element(arr []int, target int) bool{
    for _, x := range arr{
        if x == target{
            return true
        }
    }

    return false
}
