/**
 * @param {Function} fn
 * @return {Function}
 */
var curry = function(fn) {
    return function curried(...args) {
        if (fn.length == args.length){
            return fn.apply(this,args)
        } else {
            return (...args2) => {
                return curried.apply(this, args.concat(args2))
            }
        }

    };
};

/**
 * function sum(a, b) { return a + b; }
 * const csum = curry(sum);
 * csum(1)(2) // 3
 */
