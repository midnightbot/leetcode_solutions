func findTheDifference(s string, t string) byte {
    m := make(map[int]int)

    for _, val := range s{
        _,present := m[int(val)]
        if present{
            m[int(val)]+=1
        } else {
            m[int(val)] = 1
        }
    }

    for _, val := range t{
        _,present := m[int(val)]
        if present{
            m[int(val)]-=1
        } else {
            m[int(val)] = -1
        }
    }

    for key,val := range m{
        if val == -1{
            return byte(key)
        }
    }


    return byte(0)
}
