/**
 * @param {number} n
 * @yields {number}
 */
function* factorial(n) {
    if (n==0){
        yield 1;
    } else {
        let result = 1;
        for(let i=1;i<=n;i++){
            result*=i;
            yield result;
        }
    }
};


/**
 * const gen = factorial(2);
 * gen.next().value; // 1
 * gen.next().value; // 2
 */
