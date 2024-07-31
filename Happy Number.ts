function isHappy(n: number): boolean {
    let copies = [n];
    n = get_sum(n);
    if(n === 1) return true;

    while(!copies.includes(n)) {

        if(n === 1) {
            return true;
        }
        copies.push(n);

        n = get_sum(n);
    }

    return false;
};
const get_sum = (num : number) => {
    let sum = 0;
    for(let n of num.toString()) {
        sum += Number(n) ** 2;
    }
    return sum;
}
