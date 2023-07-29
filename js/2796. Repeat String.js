String.prototype.replicate = function(times) {
    var ans = '';
    for(let i=0;i<times;i++){
        ans+=this;
    }
    return ans;
}
