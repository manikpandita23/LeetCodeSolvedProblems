/**
 * @param {number[]} mapping
 * @param {number[]} nums
 * @return {number[]}
 */
var sortJumbled = function(mapping, nums) {
    const getMappedValue = (num) => {
        let mappedStr = '';
        for (const char of num.toString()) {
            mappedStr += mapping[char];
        }
        return parseInt(mappedStr);
    };
    return nums.slice().sort((a, b) => {
        const mappedA = getMappedValue(a);
        const mappedB = getMappedValue(b);
        return mappedA - mappedB;
    });
};
let mapping = [8,9,4,0,2,1,3,5,7,6];
let nums = [991, 338, 38];
console.log(sortJumbled(mapping, nums)); 
mapping = [0,1,2,3,4,5,6,7,8,9];
nums = [789, 456, 123];
console.log(sortJumbled(mapping, nums));  
