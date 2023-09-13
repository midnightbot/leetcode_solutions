/**
 * @param {Array<Function>} functions
 * @param {number} ms
 * @return {Array<Function>}
 */
var delayAll = function(functions, ms) {
    return functions.map(
        (fn) => () =>
        new Promise((resolve,reject) => {
            setTimeout(() => {
                fn().then(resolve).catch(reject);
            },ms);
        })
    );
};

