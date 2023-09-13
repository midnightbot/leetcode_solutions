/**
 * @param {Object} obj
 * @return {Object}
 */
var invertObject = function(obj) {
    const ans = {};
    for(let key in obj){
        const val = obj[key].toString();
        if (val in ans){
            ans[val] = Array.isArray(ans[val]) ? [ ...ans[val],key] : [ans[val],key.toString()];
        }
        else {
            ans[val] = key.toString();
        }
    }

    return ans;
};
