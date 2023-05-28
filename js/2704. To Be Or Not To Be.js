/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    function toBe(val1){
        if(val === val1){
            return true
        } else {
            throw new Error("Not Equal")
        }
    }
    
    function notToBe(val1){
        if(val !== val1){
            return true
        } else {
            throw new Error("Equal")
        }
    }
    
    return {toBe, notToBe}
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */
