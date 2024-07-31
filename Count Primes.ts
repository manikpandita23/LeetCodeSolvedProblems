var countPrimes = function(n) {
     if (n < 3) return 0;
    
    const count = new Uint8Array(n);
    let res = 1;
    
    for (let i = 3; i < n; i += 2) {
        if (!count[i]) {
            res++;
            for (let j = i * i; j < n; j += 2 * i) {
                count[j] = 1;
            }
        }
    }
    
    return res;
};
