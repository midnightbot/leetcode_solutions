/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array[]}
 */
var chunk = function(arr, size) {
    let ans = [];
    let tmp = [];
    for(let i=0;i<arr.length;i++){
        tmp.push(arr[i]);
        if(tmp.length == size){
            ans.push(tmp);
            tmp = [];
        }
    }
    if(tmp.length>0){
        ans.push(tmp);
    }
    return ans;
};
