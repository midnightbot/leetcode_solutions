/**
 * @param {any[]} arr
 * @param {number} depth
 * @return {any[]}
 */
var flat = function (arr, n) {
    if (n==0){
        return arr;
    }
    let ans = [];

    for(let it of arr){
        if(Array.isArray(it)){
            ans.push(...flat(it, n-1));
        } else {
            ans.push(it);
        }
    }
    return ans;
    
};
