/**
 * @param {Object | Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    if(Array.isArray(obj)){
        return !(obj.length);
    }
    return !(Object.keys(obj).length);
};
