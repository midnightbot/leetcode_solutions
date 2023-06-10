func isFascinating(n int) bool {
    ans:=strconv.Itoa(n) + strconv.Itoa(2*n) + strconv.Itoa(3*n)
    for i:=1;i<=9;i++ {
        if(!strings.Contains(ans, strconv.Itoa(i))){
            return false
        }
    }
    return len(ans) == 9 
}
