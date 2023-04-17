/**
 * @param {Function} fn
 * @return {Array}
 */
Array.prototype.groupBy = function(fn) {
    const ans = {};

    for(let x of this){
        const key = fn(x);

        if (ans[key] === undefined){
            ans[key] = [x];
        } else {
            ans[key].push(x);
        }
    }
    return ans;  
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */
