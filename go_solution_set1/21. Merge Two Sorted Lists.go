/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 import(
     "fmt"
 )
 func create_ll(indx int, nums[] int) *ListNode{
     if (indx == len(nums)){
         return nil
     } else {
         var new_node *ListNode
         new_node = new(ListNode)
         new_node.Val = nums[indx]
         new_node.Next = create_ll(indx+1, nums)
         return new_node
     }
 }
func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
    temp1 := []int{}
    temp2 := []int{}
    for list1 != nil{
        temp1 = append(temp1, list1.Val)
        list1 = list1.Next
    }

    for list2 != nil{
        temp2 = append(temp2, list2.Val)
        list2 = list2.Next
    }
    // combine both the arrays in temp1
    for _, it := range temp2{
        temp1 = append(temp1, it)
    }
    sort.Ints(temp1)

    return create_ll(0, temp1)
}
