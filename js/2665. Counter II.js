/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let i = init;
    let counter = init;

    function increment(){
        counter+=1;
        return counter;
    }

    function decrement(){
        counter-=1;
        return counter;
    }

    function reset(){
        counter = i;
        return counter;
    }

    return {increment, decrement, reset};
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */
