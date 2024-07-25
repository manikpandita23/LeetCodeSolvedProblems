/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArray = function(nums) {
    const merge = (left, right) => {
        let sorted = [];
        let i = 0, j = 0;
        while (i < left.length && j < right.length) {
            if (left[i] < right[j]) {
                sorted.push(left[i]);
                i++;
            } else {
                sorted.push(right[j]);
                j++;
            }
        } 
        return sorted.concat(left.slice(i)).concat(right.slice(j));
    };
    const mergeSort = (array) => {
        if (array.length <= 1) {
            return array;
        }
        const mid = Math.floor(array.length / 2);
        const left = mergeSort(array.slice(0, mid));
        const right = mergeSort(array.slice(mid));
        return merge(left, right);
    };
    return mergeSort(nums);
};
console.log(sortArray([5, 2, 3, 1]));  
console.log(sortArray([5, 1, 1, 2, 0, 0])); 
