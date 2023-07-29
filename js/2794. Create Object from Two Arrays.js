/**
 * @param {Array} keysArr
 * @param {Array} valuesArr
 * @return {Object}
 */
var createObject = function(keysArr, valuesArr) {
    const ans = {};

    for(const indx in keysArr){
        const k = String(keysArr[indx]);
        if (k in ans){
            continue;
        }
        ans[k] = valuesArr[indx]
    }
    return ans;
};
