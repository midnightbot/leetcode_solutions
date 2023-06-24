import(
    "fmt"
    "strconv"
)
func reverse_str(str string) string {
    rune_arr := []rune(str)
    var rev []rune
    for i := len(rune_arr) - 1; i >= 0; i-- {
        rev = append(rev, rune_arr[i])
    }
    return string(rev)
}
func isPalindrome(x int) bool {
    if (x < 0){
        return false
    }

    temp := strconv.Itoa(x)
    temp2 := reverse_str(temp)

    return temp == temp2
}
