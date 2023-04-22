/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
    let prev = 0;
    let next = 1;

    while (true){
        yield prev;
        [prev,next] = [next, prev + next];
    }

    
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */
