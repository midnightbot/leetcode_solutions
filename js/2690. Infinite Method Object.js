/**
 * @return {Object}
 */
var createInfiniteObject = function() {
    return new Proxy({},{
        get(_,p){
            return () => String(p);
        }
    })
};

/**
 * const obj = createInfiniteObject();
 * obj['abc123'](); // "abc123"
 */
